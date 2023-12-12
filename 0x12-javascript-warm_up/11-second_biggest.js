#!/usr/bin/node
// Script that to calculate factorial of a number.
const array = process.argv.slice(2);
array.sort(function (a, b) {
  return (parseInt(b) - parseInt(a));
});
console.log(process.argv.length <= 3 ? 0 : parseInt(array[1]));
