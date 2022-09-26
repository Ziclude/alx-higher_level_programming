#!/bin/bash
#curl send POST req to URL and display response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
