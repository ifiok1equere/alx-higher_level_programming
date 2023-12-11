#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (args[2] === undefined || isNaN(Number(args[2]))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(Number(args[2])));
}
