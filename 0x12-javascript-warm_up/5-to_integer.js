#!/usr/bin/node
// Script that Check if the argument is a number then parse and print it.
if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
