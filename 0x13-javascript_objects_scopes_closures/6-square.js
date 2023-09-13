#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let i = 0;
      while (i < this.width) {
        console.log(c.repeat(this.height));
        i++;
      }
    }
  }
}

module.exports = Square;
