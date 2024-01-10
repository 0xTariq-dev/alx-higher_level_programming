#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
from urllib import request, response, parse
from sys import argv


if __name__ == "__main__":
    # encode the email argument
    data = parse.urlencode({'email': argv[2]}).encode()
    # Create a request object
    req = request.Request(argv[1], data=data)
    # Add the email argument
    req.add_header('email', argv[2])
    with request.urlopen(req) as response:
        # Print the email
        print(response.read().decode('utf-8'))
