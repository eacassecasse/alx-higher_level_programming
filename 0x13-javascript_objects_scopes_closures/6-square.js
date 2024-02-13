#!/usr/bin/node

const Rectangle = require('./4-rectangle');

const Square = class extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c == undefined) {
      super.print();
    } else {
      console.log(c);
    }
  }
};

module.exports = Square;
