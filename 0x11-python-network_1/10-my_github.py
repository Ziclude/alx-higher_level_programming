#!/usr/bin/python3
"""Script that take your github creds and github api to display id"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    autht = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get("https://api.github.com/user", autht=auth)
    print(req.json().get("id"))
