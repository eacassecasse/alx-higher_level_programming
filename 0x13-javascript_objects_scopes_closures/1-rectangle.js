#!/usr/bin/node

const Rectangle = class {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }

  set width (_width) {
    this.width = _width;
  }

  get width () {
    return this.width;
  }

  set height (_height) {
    this.height = _height;
  }

  get height () {
    return this.height;
  }
};

module.exports = Rectangle;
