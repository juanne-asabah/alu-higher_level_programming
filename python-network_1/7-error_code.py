#!/usr/bin/python3
"""
This module takes a URL, sends an HTTP request using the requests package,
and displays the response body or its error code if it is >= 400.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
