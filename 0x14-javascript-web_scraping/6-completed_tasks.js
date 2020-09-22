#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const dict = {};
    for (const task of JSON.parse(body)) {
      if (task.completed === true) {
        if (isNaN(dict[task.userId])) {
          dict[task.userId] = 1;
        } else {
          dict[task.userId] += 1;
        }
      }
    }
    console.log(dict);
  }
});
