#!/usr/bin/python3
"""
This module takes a URL and an email address, sends a POST request
using the requests package, and displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    payload = {"email": sys.argv[2]}

    response = requests.post(url, data=payload)
    print(response.text)
