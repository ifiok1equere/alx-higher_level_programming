#!/usr/bin/node

const process = require('process');
const args = process.argv;

let MaxInt = Number.MIN_SAFE_INTEGER;
let MaxIntNext = Number.MIN_SAFE_INTEGER;

if (args.length < 4) {
  console.log(0);
} else {
  for (let i = 0; i <= args.length - 2; i++) {
    if (MaxInt < parseInt(args[i + 2])) {
      MaxInt = parseInt(args[i + 2]);
    }
  }
  for (let i = 0; i <= args.length - 2; i++) {
    if (((parseInt(args[i + 2])) > MaxIntNext) && (parseInt(args[i + 2]) < MaxInt)) {
      MaxIntNext = parseInt(args[i + 2]);
    }
  }
}
/* console.log(MaxInt); */
console.log(MaxIntNext);
