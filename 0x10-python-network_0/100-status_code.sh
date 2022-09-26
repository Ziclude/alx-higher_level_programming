#!/bin/bash
# send req to a url and display response
curl -s -o /dev/null -w "%{http_code}" "$1"
