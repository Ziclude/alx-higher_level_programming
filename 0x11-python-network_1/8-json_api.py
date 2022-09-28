#!/usr/bin/python3
"""script that takes in letter and send Post req"""
import sys
import requests


if __name__ == "__main__":
    ltr = "" if len(sys.argv) == 1 else sys.argv[1]
    pld = {"q": ltr}

    req = requests.post("http://0.0.0.0:5000/search_user", data=pld)
    try:
        resp = req.json()
        if resp == {}:
            print("No result")
        else:
            print("[{}] {}".format(resp.get("id"), resp.get("name")))
    except ValueError:
        print("Not a valid JSON")
