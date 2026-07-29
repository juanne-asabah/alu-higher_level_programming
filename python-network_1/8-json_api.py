#!/usr/bin/python3
"""
This module takes a letter as an argument and sends a POST request to
a local user search API, handling various JSON response scenarios.
"""
import sys
import requests


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {"q": q}

    response = requests.post("http://0.0.0", data=payload)

    try:
        json_data = response.json()
        if not json_data:
            print("No result")
        else:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
    except ValueError:
        print("Not a valid JSON")
