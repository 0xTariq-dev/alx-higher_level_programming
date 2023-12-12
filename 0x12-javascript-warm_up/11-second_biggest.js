#!/usr/bin/node
// Script that to calculate factorial of a number.
const array = process.argv.slice(2);
array.sort(function (a, b) {
   return (parseInt(b) - parseInt(a)); 
});
if (process.argv.length <= 3) { console.log(0); }
else { console.log(parseInt(array[1])); }
