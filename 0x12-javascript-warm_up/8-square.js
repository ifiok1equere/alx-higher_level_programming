#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (isNaN(Number(args[2]))) {
  console.log('Missing size');
} else {
  let i = 0;
  const count = parseInt(args[2]);
  while (i < count) {
    console.log('X'.repeat(count));
    i++;
  }
}
