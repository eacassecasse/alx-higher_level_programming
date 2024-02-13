#!/usr/bin/node

const Rectangle = class {
  constructor (w, h) {
    if (parseInt(w) > 0 && parseInt(h) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  set width (width) {
    this.width = width;
  }

  get width () {
    return this.width;
  }

  set height (height) {
    this.height = height;
  }

  get height () {
    return this.height;
  }
};

module.exports = Rectangle;
