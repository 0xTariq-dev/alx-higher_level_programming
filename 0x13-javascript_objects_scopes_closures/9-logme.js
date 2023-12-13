#!/usr/bin/node
const arr = [];
exports.logMe = function (item) {
  arr.push(item);
  console.log(`${arr.indexOf(item)}: ${item}`);
};
