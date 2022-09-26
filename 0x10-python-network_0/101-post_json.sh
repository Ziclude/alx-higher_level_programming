#!/bin/bash
# send JSON POST req to url and display response
curl -sL -H "content-type:application/json" -d @"$2" -X POST "$1"
