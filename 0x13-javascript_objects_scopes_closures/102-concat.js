#!/usr/bin/node

const fs = require('fs');

if (process.argv.length < 5) {
  process.exit(1);
}

const fileA = fs.openSync(process.argv[2], 'r');
const fileB = fs.openSync(process.argv[3], 'r');
const fileC = fs.openSync(process.argv[4], 'w');

const contents1 = fs.readFileSync(fileA, 'utf8');
const contents2 = fs.readFileSync(fileB, 'utf8');

fs.writeFileSync(fileC, contents1 + contents2);

fs.closeSync(fileA);
fs.closeSync(fileB);
fs.closeSync(fileC);
