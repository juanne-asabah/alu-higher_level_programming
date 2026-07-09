#!/usr/bin/python3
for ascii_code in range(97, 123):
    if ascii_code != 113 and ascii_code != 101:
        print("{}".format(chr(ascii_code)), end="")
