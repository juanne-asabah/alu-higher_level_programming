#!/usr/bin/python3
"""
This module takes a URL as an argument, sends a request using the requests
package, and displays the value of X-Request-Id from the response header.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
