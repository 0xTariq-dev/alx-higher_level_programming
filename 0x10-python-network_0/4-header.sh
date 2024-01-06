#!/bin/bash
# This script will send GET request with a custom variable in the header.
curl -X GET -H "X-School-User-Id: 98" -s "$1"
