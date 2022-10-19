#!/usr/bin/node
const fl = require('fl');
fl.readFile(process.argv[2], 'utf-8', function (error, content) {
    console.log(error || content);
});
