fs = require('fs')
fs.readFile('/Users/gselleslagh/dev/aoc/input.txt', 'utf8', function (err,data) {
  if (err) {
    return console.log(err);
  }
  const arr = data.split('\n')
  let elves = [];
  let current = 0;
  arr.map((item) => {
    if (!isNaN(parseInt(item))) {
        current += parseInt(item)
    } else {
        elves.push(current)
        current = 0
    }
  })
  elves.sort(compareFn)
  const length = elves.length
  const p1 = elves[length - 1]
  const p2 = elves[length - 1] + elves[length - 2] + elves[length - 3]
  console.log("Part 1: ", p1)
  console.log("Part 2: ", p2)
});



function compareFn(a, b) {
    return a-b
  }
