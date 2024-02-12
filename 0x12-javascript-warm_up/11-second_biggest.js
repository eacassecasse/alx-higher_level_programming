#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length <= 3) {
  console.log(0);
} else {
  let first = 0;
  let second = 0;

  for (let i = 2; i < argv.length; i++) {
    if (argv[i] > first) {
      second = first;
      first = argv[i];
    }
  }

  console.log(second);
}
