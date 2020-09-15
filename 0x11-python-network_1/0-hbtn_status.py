#!/usr/bin/python3
"""
fetches hbtn
"""
import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        s = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(s)))
        print("\t- content: {}".format(s))
        print("\t- utf8 content: {}".format(s.decode("utf-8")))
