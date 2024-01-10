#!/usr/bin/python3
"""
    Fetches https://alx-intranet.hbtn.io/status
    and displays the response's body
"""
from urllib import request, response


if __name__ == "__main__":
    # Create a request object
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()  # Read the response
        # Print the formated response
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
