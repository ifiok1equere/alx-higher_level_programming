#!/usr/bin/node

const process = require('process');
const args = process.argv;

(function add (a, b) {
  if (args.length !== 4 || isNaN(args[2]) || isNaN(args[3])) {
    console.log('NaN');
  } else {
    console.log(parseInt(args[2]) + parseInt(args[3]));
  }
})();
