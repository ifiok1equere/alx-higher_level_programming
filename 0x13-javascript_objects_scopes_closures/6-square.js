#!/usr/bin/node

const PreviousSquare = require('./5-square');

class Square extends PreviousSquare {
  charPrint (c) {
    if (c === undefined) {
      super.print(c);
    } else {
      let i = 0;
      while (i < this.height) {
        console.log(c.repeat(this.height));
        i++;
      }
    }
  }
}

module.exports = Square;
