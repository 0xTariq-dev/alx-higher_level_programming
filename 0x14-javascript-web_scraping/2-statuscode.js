#!/usr/bin/node
// Script that display the status code of a GET request.

const request = require('request');
const url = process.argv[2];

request(url, function (err, response) {
  if (err) {
    console.log(err);
  }
  console.log('code:', response.statusCode);
});
