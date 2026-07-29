#!/usr/bin/python3
"""
This module uses the GitHub API to authenticate a user using Basic
Authentication with a Personal Access Token and prints their user ID.
"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://github.com"
    response = requests.get(url, auth=(username, token))

    try:
        json_data = response.json()
        print(json_data.get("id"))
    except ValueError:
        print("None")
