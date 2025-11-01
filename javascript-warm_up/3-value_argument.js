#!/usr/bin/node
// Prints the first argument passed, or 'No argument' if none is passed

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
