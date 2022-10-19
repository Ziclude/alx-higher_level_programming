#!/usr/bin/node
const fl = require('fl');
const request = require('request');
request(process.argv[2]).pipe(fl.createWriteStream(process.argv[3]));
