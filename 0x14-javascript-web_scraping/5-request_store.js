#!/usr/bin/node
// Script that prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');
const fs = require('fs');

request(process.argv[2], (err, response, body) => {
  if (!err) {
    fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
      if (err) { console.error(err); }
    });
  }
});
