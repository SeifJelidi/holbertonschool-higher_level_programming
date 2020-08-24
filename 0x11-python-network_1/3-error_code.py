#!/usr/bin/python3
"""
____
"""
import urllib.request
import urllib.error
import sys
if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as rps:
            html5 = rps.read()
            print(html5.decode("utf-8"))
    except error.HTTPError as x:
        print("Error code: {}".format(x.code))
