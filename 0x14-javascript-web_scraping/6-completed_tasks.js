#!/usr/bin/node
// Script that prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (response.statusCode === 200) {
    const completed = {};
    const todos = JSON.parse(body);
    for (const i in todos) {
      const todo = todos[i];
      if (todo.completed === true) {
        if (completed[todo.userId] === undefined) {
          completed[todo.userId] = 1;
        } else {
          completed[todo.userId]++;
        }
      }
    }
    console.log(completed);
  } else if (err) {
    console.log('Error:', err);
  } else {
    console.log('Error with code: ' + response.statusCode);
  }
});
