#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const moviesJson = JSON.parse(body);
    let c = 0;
    for (let i = 0; i < moviesJson.count - 1; i++) {
      for (let j = 0; j < moviesJson.results[i].characters.length; j++) {
        const sp = moviesJson.results[i].characters[j].split('/');
        if (sp[5] === '18') {
          c++;
        }
      }
    }
    console.log(c);
  }
});
