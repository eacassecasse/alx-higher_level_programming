#!/usr/bin/node

const { argv } = require('node:process');
let count = 0;

argv.map(() => count++);

if (count <= 2) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
