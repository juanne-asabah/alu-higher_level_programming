#!/usr/bin/python3
"""Fetches a URL status provided as an argument using the requests package."""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        response = requests.get(url)
        text = response.text
        print("Body response:")
        print("\t- type: {}".format(type(text)))
        print("\t- content: {}".format(text))
