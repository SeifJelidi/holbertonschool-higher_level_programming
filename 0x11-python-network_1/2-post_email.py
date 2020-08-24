#!/usr/bin/python3
"""
displays X-Request-id's value
"""
import urllib.request
import urllib.parse
from sys import argv
if __name__ == "__main__":

    data = parse.urlencode({'email': sys.argv[2]}).encode()
    req = request.Request(sys.argv[1], data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
