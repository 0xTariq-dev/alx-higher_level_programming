#!/usr/bin/node
// Read the content of a file and print it to the stdout

const filePath = process.argv[2];
const fs = require('fs');

fs.open(filePath, 'r', (err, fd) => {
    if (err) {
        console.error(err);
    } else {
        console.log(fs.readFileSync(fd, 'utf8'));
        fs.close(fd);
    }
});
