#!/usr/bin/python3
"""Sends a POST request to a search API with a letter parameter."""
import sys
import requests


if __name__ == "__main__":
    q = sys.argv if len(sys.argv) > 1 else ""
    url = "http://0.0.0"
    payload = {'q': q}

    try:
        response = requests.post(url, data=payload)
        json_data = response.json()

        if json_data == {} or not json_data:
            print("No result")
        else:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
    except ValueError:
        print("Not a valid JSON")
