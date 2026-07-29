#!/usr/bin/python3
"""
This module takes a URL as an argument, sends a request to it, and displays
the body of the response in UTF-8. It gracefully catches urllib HTTP errors.
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
