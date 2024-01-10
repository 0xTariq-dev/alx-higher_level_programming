#!/usr/bin/python3
"""sends a request to the passed URL and displays the body of the response"""
from urllib import request, error
from sys import argv


if __name__ == "__main__":
    # Create a request object
    try:
        with request.urlopen(argv[1]) as r:
            print(r.read().decode("utf-8"))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
