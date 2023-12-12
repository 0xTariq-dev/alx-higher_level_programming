#!/usr/bin/node
// Script that Check the existance of command-line arguments.

const { argv } = require('node:process');

if (argv.length === 2) { console.log('No argument'); }
else if (argv.length === 3) { console.log('Argument found'); }
else { console.log('Arguments found'); }
