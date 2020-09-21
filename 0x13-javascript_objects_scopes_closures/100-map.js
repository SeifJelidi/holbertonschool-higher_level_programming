#!/usr/bin/node
const newList = require('./100-data').list;
const result = newList.map(function (element, index) {
  return element * index;
});
console.log(newList);
console.log(result);
