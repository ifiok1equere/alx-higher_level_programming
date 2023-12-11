#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (args[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < args[2]) {
    console.log('C is fun');
    i++;
  }
}
