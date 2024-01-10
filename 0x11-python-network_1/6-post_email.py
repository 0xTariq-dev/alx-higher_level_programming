#!/usr/bin/python3
"""
    Module that fetches a URL using requests package and displays
    the value of the variable email in the response header
"""
import requests
from sys import argv


if __name__ == "__main__":
    data = {'email': argv[2]}
    # Create a request object
    req = requests.post(argv[1], data=data)
    # Print the email from the response header
    print(req.text)
