#!/bin/bash
# ends a request to a URL displaying size of response body.
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
