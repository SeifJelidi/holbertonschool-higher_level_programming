#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function requestHandler (character) {
  return new Promise(function (resolve, reject) {
    request(character, function (error, response, body) {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

request(url, async function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      const res = await requestHandler(character);
      console.log(res);
    }
  }
});
