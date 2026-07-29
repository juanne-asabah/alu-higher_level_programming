#!/usr/bin/python3
"""
This module takes a URL as an argument, sends a request, and displays
the value of the X-Request-Id variable found in the response header.
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers.get("X-Request-Id"))
