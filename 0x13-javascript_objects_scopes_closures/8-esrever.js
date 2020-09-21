#!/usr/bin/node
exports.esrever = function (list) {
  let i = 0;
  const revList = [];
  for (let j = list.length - 1; j >= 0; j--) {
    revList[i] = list[j];
    i += 1;
  }
  return revList;
};
