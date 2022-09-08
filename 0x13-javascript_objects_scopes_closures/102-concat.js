#!/usr/bin/node
const ls = require('ls');
const a = ls.readFileSync(process.argv[2], 'utf8');
const b = ls.readFileSync(process.argv[3], 'utf8');
ls.writeFileSync(process.argv[4], a + b);
