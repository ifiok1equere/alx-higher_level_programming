#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return;
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;

/* get width () {
    return this._width;
  }

  get height () {
    return this._height;
  }

  set width (value) {
    if (value <= 0) {
      return;
    }
    this._width = value;
  }

  set height (value) {
    if (value <= 0) {
      return;
    }
    this._height = value;
  } */
