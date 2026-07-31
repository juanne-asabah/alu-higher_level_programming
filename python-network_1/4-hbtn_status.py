#!/usr/bin/python3
"""Fetches a URL status using the requests package."""
import requests


if __name__ == "__main__":
    url = 'https://hbtn.io'
    try:
        import sys
        if len(sys.argv) > 1:
            url = sys.argv[1]
    except Exception:
        pass

    response = requests.get(url)
    text = response.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
