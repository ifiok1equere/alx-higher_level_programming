#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (args[2] === undefined || isNaN(Number(args[2]))) {
  console.log('Missing size');
} else {
  let i = 0;
  const count = parseInt(args[2]);
  while (i < count) {
    console.log('x'.repeat(count));
    i++;
  }
}
