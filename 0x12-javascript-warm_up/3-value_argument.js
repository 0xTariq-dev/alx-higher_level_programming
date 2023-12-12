#!/usr/bin/node
// Script that Check the existance of arguments and print the first arg.
if (process.argv.length === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
