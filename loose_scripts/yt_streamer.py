# Youtube playlist player
# Randomises a youtube playlist and streams it to VLC player
#
# Notes:
# Currently, the playlist id has been hardcoded meaning it only works on one playlist (although this is can be changed).
# The code to delete the playlist after opening vlc is commented out as I am not sure whether I want to keep the playlist or not.
# This has not been tested (yet) with a public playlist so I do not know how the authorization works with one.
# The 'client_info' file is obtained after creating a google cloud project. See the client_info_layout_example.json for the layout of the file.
#
# Misc. Links:
# Why use dict.get('example') over dict['example']: https://stackoverflow.com/a/11041421
# Youtube api playlistItem docs: https://developers.google.com/youtube/v3/docs/playlistItems/list
# Youtube playlist link (private): https://www.youtube.com/playlist?list=PLuSnN_Do2dTgNJ0Fiipd050oaQ6CX_F5P
# VLC command line docs: https://wiki.videolan.org/VLC_command-line_help/
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

##### Authorization variables #####
# client_info.json also contains two redirect uris but there is no reason not to hard code
with open('client_info.json') as info:
    client_info = json.load(info)
client_id = client_info.get('installed', {}).get('client_id')
client_secret = client_info.get('installed', {}).get('client_secret')
redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'

authorization_base_url = 'https://accounts.google.com/o/oauth2/v2/auth'
token_url = 'https://www.googleapis.com/oauth2/v4/token'
scope = 'https://www.googleapis.com/auth/youtube'
auth_url = authorization_base_url + '?client_id={ci}&redirect_uri={ru}&response_type={rt}&scope={s}'.format(ci=client_id, ru=redirect_uri, rt='code', s=scope)

##### Get an access token #####
# Open a new browser tab to allow the user to give permission to the app (or decline)
webbrowser.open(auth_url, new=2)
# If the user gave the app permission they will be shown a code on-screen
auth_code = input('Please enter the code provided: ')

response = requests.post(token_url + '?code={code}&client_id={ci}&client_secret={cs}&redirect_uri={ru}&grant_type=authorization_code'.format(code=auth_code, ci=client_id, cs=client_secret, ru=redirect_uri))
data = response.json()

# The auth headers will be sent with every request
authorization_header = {'Authorization': 'Bearer {token}'.format(token=data.get('access_token'))}
playlist = []
next_page = True
page_token = ''

##### Create the playlist #####
print('Getting playlist ids...')
while next_page:
    playlist_json = requests.get('https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&playlistId=PLuSnN_Do2dTgNJ0Fiipd050oaQ6CX_F5P&maxResults=50&pageToken=' + page_token, headers=authorization_header)
    playlist_data = playlist_json.json()

    for video in playlist_data.get('items'):
        playlist.append(video.get('contentDetails', {}).get('videoId'))

    # nextPageToken is only in the response if there is a next page
    if playlist_data.get('nextPageToken') is not None:
        page_token = playlist_data.get('nextPageToken')
    else:
        next_page = False
        print('Playlist ids retrieved.')

# Randomise urls
random.shuffle(playlist)

# Create a .m3u playlist file
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
print('Playlist successfully created.')

print('Opening playlist in vlc...')
# If the path to VLC is not in PATH environment variable, the full path must be provided
VLC_PATH = 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'
# '--no-video' and '--qt-start-minimized' are VLC command line arguments that can be removed if needed/wanted
ARGS = [VLC_PATH, '--no-video', '--qt-start-minimized', 'yt_playlist.m3u']
# Alternative (If VLC's path is in the PATH variable) version
# ARGS = ['vlc', '--no-video', '--qt-start-minimized', 'yt_playlist.m3u']
subprocess.run(ARGS)

# print('Removing playlist file...')
# os.remove('yt_playlist.m3u')

input('\n\nPress enter to exit')
