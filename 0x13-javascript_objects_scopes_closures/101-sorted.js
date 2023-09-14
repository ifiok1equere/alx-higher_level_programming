#!/usr/bin/node

const importedDict = require('./101-data').dict;

const valueList = Object.values(importedDict);
const newDict = {};
let newArray2 = [];

for (let i = 0; i < valueList.length; i++) {
  const newArray = [];
  for (const key in importedDict) {
    if (importedDict[key] === valueList[i]) {
      newArray.push(key);
    }
  }
  newArray2 = newArray;
  newDict[valueList[i]] = newArray2;
}

console.log(newDict);
