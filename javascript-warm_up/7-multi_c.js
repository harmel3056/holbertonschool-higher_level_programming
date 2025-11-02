#!/usr/bin/node
// Prints a string the quantity of times entered on the command line

const string = 'C is fun';
const printNo = Number(process.argv[2]);

if (isNaN(printNo)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < printNo; i++) {
    console.log(string);
  }
}
