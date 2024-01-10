#!/usr/bin/python3
"""sends a request to the passed URL and displays the body of the response"""
from urllib import request, response, error
from sys import argv


if __name__ == "__main__":
    # Create a request object
    req = request.Request(argv[1])
    try:
        request.urlopen(req)
    except error.HTTPError as e:
        if hasattr(e, 'code'):
            print("Error code: {}".format(e.code))
    else:
        print("Index")
