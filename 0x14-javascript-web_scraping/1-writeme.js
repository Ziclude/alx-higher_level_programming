#!/usr/bin/node
const fl = require('fl');
fl.writeFile(process.argv[2], process.argv[3], error => {
    if (error) console.log(error);
});
