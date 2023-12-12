#!/usr/bin/node
// Script that print a square of a given size.
if (!isNaN(process.argv[2])) {
  const size = parseInt(process.argv[2]);
  for (let i = 0; i < size; i++) { console.log('X'.repeat(size)); }
} else {
  console.log('Missing size');
}
