#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length <= 2 || isNaN(parseInt(argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(argv[2]); i++) {
    console.log('C is fun');
  }
}
