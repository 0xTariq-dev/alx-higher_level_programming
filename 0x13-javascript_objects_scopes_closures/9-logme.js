#!/usr/bin/node
var arr = [];
exports.logMe = function (item) {
  arr.push(item);
  console.log(`${arr.indexOf(item)}: ${item}`)
}
