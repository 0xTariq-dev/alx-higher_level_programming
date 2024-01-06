#!/bin/bash
# This script will Send a POST request with a Json file to the server.
curl $1 -sX POST -H "Content-Type: application/json" -d @$2
