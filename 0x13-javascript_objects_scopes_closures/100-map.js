#!/usr/bin/node

const importList = require('./100-data').list;

let i = -1;
const newList = importList.map((x) => {
  i++;
  return x * i;
});
console.log(importList);
console.log(newList);
