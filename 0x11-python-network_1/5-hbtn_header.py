#!/usr/bin/python3
"""
    Module that fetches a URL using requests package and displays
    the value of the variable X-Request-Id in the response header
"""
import requests
from sys import argv


if __name__ == "__main__":
    # Create a request object
    req = requests.get(argv[1])
    # Print the request id
    print(req.headers.get('X-Request-Id'))
