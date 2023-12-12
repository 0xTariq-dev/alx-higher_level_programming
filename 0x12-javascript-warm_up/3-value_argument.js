#!/usr/bin/node
// Script that Check the existance of arguments and print the first arg.
if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
