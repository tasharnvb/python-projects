# Youtube playlist player
# Randomises and streams a youtube Music playlist to VLC player
#
# Pseudocode -
# Get all items (videos) from the Music playlist
# Save video urls in a list
# Create a m3u playlist file with urls
# Open playlist in vlc
# Delete playlist when finished(?)
#
# To-do
# Clean up code (add/clean up comments, consistent formatting, error checking)
# Change subprocess.run to .Popen so that the script can end after opening vlc: https://stackoverflow.com/a/9280294
# Add error checking (See yt_error.json)
# Let the user specify their own playlist url (ask user for full url or just playlist id?)
# Allow for both public and private playlists to be used (Note: auth not needed with public playlists)
#   How to determine if a playlist is public or private before auth?
#       Read client info from args instead of file? if there is 1 then assume public? 2 assume private?
#       (A GUI would solve this easily: radio button for public or private)
#   If the playlist is private, go through the normal authorization process
#   If the playlist is public, skip the authorization and use a different request url format
#       public playlist request url example: https://www.googleapis.com/youtube/v3/playlistItems?playlistId={playlist_id}&key={api_key}
# Try to reimplement using google's python client library
# Store the access and refresh tokens so that the auth can be skipped (by using the refresh token) after the user grants access
# Make a GUI (Maybe, input box for playlist url, radio button for public or private, input box for auth code, radio button for deleting playlist after streaming)

import json
import webbrowser
import random
import subprocess
# import os
import requests

with open('client_info.json') as info:
    client_info = json.load(info)
# nested get from a dictionary - https://stackoverflow.com/a/25833661
# why dict.get('example') over dict['example'] - https://stackoverflow.com/a/11041421
client_id = client_info.get('installed', {}).get('client_id')
client_secret = client_info.get('installed', {}).get('client_secret')
redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'

authorization_base_url = 'https://accounts.google.com/o/oauth2/v2/auth'
token_url = 'https://www.googleapis.com/oauth2/v4/token'
scope = 'https://www.googleapis.com/auth/youtube'
auth_url = authorization_base_url + '?client_id={ci}&redirect_uri={ru}&response_type={rt}&scope={s}'.format(ci=client_id, ru=redirect_uri, rt='code', s=scope)

webbrowser.open(auth_url, new=2)

auth_code = input('Please enter the code provided: ')

response = requests.post(token_url + '?code={code}&client_id={ci}&client_secret={cs}&redirect_uri={ru}&grant_type=authorization_code'.format(code=auth_code, ci=client_id, cs=client_secret, ru=redirect_uri))

data = response.json()
authorization_header = {'Authorization': 'Bearer {token}'.format(token=data.get('access_token'))}
# playlist_url = input('Enter the playlist URL here:')
# music_playlist_id = 'PLuSnN_Do2dTgNJ0Fiipd050oaQ6CX_F5P'
playlist = []
page_token = ''
next_page = True

print('Creating playlist...')
while next_page:
    # youtube playlistItem docs - https://developers.google.com/youtube/v3/docs/playlistItems/list
    playlist_json = requests.get('https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&playlistId=PLuSnN_Do2dTgNJ0Fiipd050oaQ6CX_F5P&maxResults=50&pageToken=' + page_token, headers=authorization_header)
    playlist_data = playlist_json.json()

    for video in playlist_data.get('items'):
        playlist.append(video.get('contentDetails', {}).get('videoId'))

    if playlist_data.get('nextPageToken') is not None:
        page_token = playlist_data.get('nextPageToken')
    else:
        next_page = False
        print('Playlist created.')

# print(playlist)

# randomise urls
random.shuffle(playlist)

# add to .m3u file
try:
    print('Creating playlist file...')
    playlist_file = open('yt_playlist.m3u', 'w', encoding='utf-8')
except Exception as e:
    print('Error: File not created.')
    print(e)
else:
    with playlist_file:
        for song_id in playlist:
            playlist_file.write('https://www.youtube.com/watch?v=' + song_id + '\n')

# open vlc with the playlist
print('Opening playlist in vlc...')
# needed if vlc is not in PATH (I think)
VLC_PATH = 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'
ARGS = [VLC_PATH, '--no-video', '--qt-start-minimized', 'yt_playlist.m3u']
# alt version
# ARGS = ['vlc', '--no-video', '--qt-start-minimized', 'yt_playlist.m3u']
subprocess.run(ARGS)

# print('Removing playlist file...')
# os.remove('yt_playlist.m3u')

input('\n\nPress enter to exit')
