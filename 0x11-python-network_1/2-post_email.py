#!/usr/bin/python3
"""
displays X-Request-id's value
"""
import urllib.request
import urllib.parse
from sys import argv
if __name__ == "__main__":

    data = urllib.parse.parse_qs.urlencode({'email': sys.argv[2]}).encode()
    req = request.Request(argv[1], data=data, method='POST')
    with urllib.request.urlopen(data.argv[2], req) as response:
        print(response.read().decode('utf-8'))
