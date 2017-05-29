# API practice
# An application to help me practice using the requests library with an API
#
# Notes:
# I made this a function just in case I wanted to expand on this (add other functions) later.
# Code adapted from: https://www.dataquest.io/blog/python-api-tutorial/
# API used for practice: https://jsonplaceholder.typicode.com/

import requests

# The base url
BASE_URL = 'https://jsonplaceholder.typicode.com'

def get_users():
    """Get all users and display their names and ids."""
    url = BASE_URL + '/users'

    response = requests.get(url)
    # Convert the response into a python object
    data = response.json()
    if response.status_code != 200:
        print('Error:')
        print(data)
    else:
        for user in data:
            print('User ID: ' + str(user['id']) + ', Name: ' + user['name'])
#        print('-----')
#        print(data)

get_users()
input('\n\nPress enter to exit')
