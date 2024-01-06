#!/bin/bash
# This script will display all accepted HTTP mothods from the server passed to it.
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
