#!/usr/bin/node
// Computes and prints a factorial using recursion

const f = Number(process.argv[2]);

function factorial (f) {
  if (isNaN(f)) {
    return 1;
  }
  // Base to stop recursion
  if (f === 0 || f === 1) {
    return 1;
  }
  return f * factorial(f - 1);
}

console.log(factorial(f));
