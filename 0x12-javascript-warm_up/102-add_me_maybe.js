#!/usr/bin/node

function addMeMaybe (num, callback) {
  num = num + 1;
  global.num = num;
  callback(num);
}
module.exports = {
  addMeMaybe
};
