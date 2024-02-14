#!/usr/bin/node

const Rectangle = class {
  constructor (w, h) {
    if (parseInt(w) > 0 && parseInt(h) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  set width (w) {
    this.width = w;
  }

  get width () {
    return this.width;
  }

  set height (h) {
    this.height = h;
  }

  get height () {
    return this.height;
  }	

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const aux = this.height;
    this.height = this.width;
    this.width = aux;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};

module.exports = Rectangle;
