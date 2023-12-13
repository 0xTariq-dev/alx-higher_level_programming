#!/usr/bin/node

const exec = require('child_process').exec;
exec(
  `cat ${process.argv[2]} ${process.argv[3]} > ${process.argv[4]}`,
  { encoding: 'buffer' }
);
