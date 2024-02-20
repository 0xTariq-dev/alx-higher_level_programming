#!/usr/bin/node
// Script that prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');
const episode = parseInt(process.argv[2]);
const url = 'https://swapi-api.hbtn.io/api/films/' + episode;

request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  console.log(JSON.parse(body).title);
});
