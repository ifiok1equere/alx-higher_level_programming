#!/usr/bin/node

function callMeMoby(times, callback) {
  for (let i = 0; i < times; i++) {
    callback();
  }
}

module.exports = {
  callMeMoby: callMeMoby,
};

