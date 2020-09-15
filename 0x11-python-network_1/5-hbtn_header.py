#!/usr/bin/python3
"""
fetches hbtn
"""
import requests
from sys import argv
if __name__ == "__main__":
    response = requests.get(argv[1])
    print(response.headers.get("X-Request-Id", None))
