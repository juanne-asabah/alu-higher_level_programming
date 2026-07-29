#!/usr/bin/python3
"""
This module fetches the status from a specific URL using the requests package
and prints structural information about the body response.
"""
import requests


if __name__ == "__main__":
    url = "https://hbtn.io"
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
