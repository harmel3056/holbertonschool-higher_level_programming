#!/usr/bin/node
// Prints number from string if conversion is possible

const str = process.argv[2];
const num = Number(str);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number:', num);
}
