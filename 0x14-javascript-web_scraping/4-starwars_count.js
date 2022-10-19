#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
    if (err) {
	console.log(err);
    } else if (response.statusCode === 200) {
	const movies = JSON.parse(body).results;
	let ct = 0;
	for (const movieIndex in movies) {
	    const movieChars = movies[movieIndex].characters;
	    for (const charIndex in movieChars) {
		if (movieChars[charIndex].includes('18')) {
		    ct++;
		}
	    }
	}
	console.log(ct);
    } else {
	console.log('An error occured. Status code: ' + response.statusCode);
    }
});
