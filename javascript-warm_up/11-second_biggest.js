#!/usr/bin/node
// Finds the second largest int in list of args entered on the command line

const args = process.argv.slice(2);
const nums = args.map(Number);
let high = -Infinity;
let second = -Infinity;

if (args.length <= 1) {
  console.log(0);
} else {
  for (const num of nums) {
    if (num > high) {
      second = high;
      high = num;
    } else if (num < high && num > second) {
      second = num;
    }
  }
  console.log(second);
}
