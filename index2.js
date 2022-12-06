const fs = require("fs");
const input = fs.readFileSync("./input2.txt", "utf8").split("\n");

// A Y
// B X
// C Z
// This strategy guide predicts and recommends the following:

// In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). 
// This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
// In the second round, your opponent will choose Paper (B), and you should choose Rock (X). 
// This ends in a loss for you with a score of 1 (1 + 0).
// The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
// Rock : A X
// Paper : B Y
// Scissors: C Z

// X means you need to lose, 
// Y means you need to end the round in a draw, and 
// Z means you need to win.

const values = {
    A: 1,
    X: 1,
    B: 2,
    Y: 2,
    C: 3,
    Z: 3,    
}
let count = 0;
input.map((item) => {
    const splitItem = item.split(" ")
    if (splitItem.length === 1) {
        return
    }
    console.log(splitItem)
    if (splitItem[1] === 'X') {
        if (splitItem[0] === 'A' ){
            count += 3
        }
        if (splitItem[0] === 'B') {
            count += 1
        }
        if (splitItem[0] === 'C') {
            count += 2
        }
    }
    if (splitItem[1] === 'Y') {
        if (splitItem[0] === 'A' ){
            count += 4
        }
        if (splitItem[0] === 'B') {
            count += 5
        }
        if (splitItem[0] === 'C') {
            count += 6
        }
    }
    if (splitItem[1] === 'Z') {
        if (splitItem[0] === 'A' ){
            count += 8
        }
        if (splitItem[0] === 'B') {
            count += 9
        }
        if (splitItem[0] === 'C') {
            count += 7
        }
    }
    console.log(count)
})
console.log(count)
