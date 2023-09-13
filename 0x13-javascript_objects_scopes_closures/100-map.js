#!/usr/bin/node

const importList = require('./100-data');

const newList = importList.list.map((x) => x * importList.list.indexOf(x));
console.log(importList.list);
console.log(newList);
