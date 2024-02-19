#!/usr/bin/node
const fs = require('fs');

const fiArg = fs.readFileSync(process.argv[2]).toString();
const seArg = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], fiArg + seArg);
