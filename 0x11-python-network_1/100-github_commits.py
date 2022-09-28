#!/usr/bin/python3
"""List 10 recent commits of given githubs"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    req = requests.get(url)
    comts = req.json()
    try:
        for a in range(10):
            print("{}: {}".format(
                comts[a].get("sha"),
                comts[a].get("commit").get("author").get("name"))
    except IndexError:
        pass
