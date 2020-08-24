#!/usr/bin/python3
"""
____
"""
import urllib.request
import urllib.error
from sys import argv
if __name__ == "__main__":
    url = argv[1]
    req = (url)
    try:
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as x:
        print("Error code: {}".format(x.code))
