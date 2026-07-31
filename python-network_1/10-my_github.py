#!/usr/bin/python3
"""Uses GitHub API to display user ID via Basic Authentication."""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://github.com"

    response = requests.get(url, auth=(username, token))

    try:
        user_data = response.json()
        print(user_data.get('id'))
    except ValueError:
        print("None")
