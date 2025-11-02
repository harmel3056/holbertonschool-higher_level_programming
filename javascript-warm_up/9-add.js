#!/usr/bin/node
// Adds ints from the command line

const a = process.argv[2];
const b = process.argv[3];

function add (a, b) {
  const result = parseInt(a) + parseInt(b);
  console.log(result);
}

add(a, b);
