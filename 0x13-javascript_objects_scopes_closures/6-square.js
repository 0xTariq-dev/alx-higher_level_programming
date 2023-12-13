#!/usr/bin/node

const Sq = require('./5-square');

class Square extends Sq {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    } else { super.print(); }
  }
}
module.exports = Square;
