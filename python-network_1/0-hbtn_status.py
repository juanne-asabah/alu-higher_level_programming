#!/usr/bin/python3
"""Fetches a URL status using urllib."""
import urllib.request


if __name__ == "__main__":
    url = 'https://alu-intranet.hbtn.io/status'
    try:
        import sys
        if len(sys.argv) > 1:
            url = sys.argv[1]
    except Exception:
        pass

    with urllib.request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
