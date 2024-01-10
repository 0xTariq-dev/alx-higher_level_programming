#!/usr/bin/python3
"""Fetches a URL and displays the response's request id"""
from urllib import request, response
from sys import argv


if __name__ == "__main__":
    # Create a request object
    with request.urlopen(argv[1]) as response:
        # Print the request id
        print(response.headers.get('X-Request-Id'))
