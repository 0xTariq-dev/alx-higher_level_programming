#!/usr/bin/node
// Script that prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (!err) {
    const episodes = JSON.parse(body).results;
    console.log(episodes.reduce((count, episode) => {
      return episode.characters.find((character) => character.endsWith('/18/'))
      ? count + 1 : count;
    }, 0));
  }
});
