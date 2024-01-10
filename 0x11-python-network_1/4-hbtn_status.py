#!/usr/bin/python3
"""Module that fetches https://intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    # Create a request object
    req = requests.get("https://alx-intranet.hbtn.io/status")
    # Print the type of the response
    print("Body response:")
    # Print the content of the response
    print(f"\t- type: {type(req.text)}\n\t- content: {req.text}")
