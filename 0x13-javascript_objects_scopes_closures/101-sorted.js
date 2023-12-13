#!/usr/bin/node

const dict = require('./101-data.js').dict;
// using reduce function with argument acc to accumulate object.
const newDict = Object.entries(dict).reduce((acc, [key, value]) => {
  // check if value exists a key and push value if not create a new key.
  acc[value] ? acc[value].push(key) : acc[value] = [key];
  // return the accumulator object.
  return acc;
}, {});
console.log(newDict);
