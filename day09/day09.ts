// Using AoC 2020 to ramp up with Typescript and get familiar with deno.
//
// Usage:
// ~/.deno/bin/deno run -- allow-read day09.ts

const input = await Deno.readTextFile('input.txt');


function part1(data: number[]): number  {
  for(let i: number = 0; i < data.length; i++) {
    let line: number = data[i]
    if (i > 24) {
      let sums = data.slice(i-25, i).map(
          b => {
            let aa = data.slice(i-25,i).map(a => b !== a ? b + a : 0 );
            return aa
          }
      )
      .flat()  // Turns [[1, 2], [3, 4]] to [1, 2, 3, 4]
      .filter((v, i, a) => a.indexOf(v) === i)  // Makes elements unique
      .sort((a, b) => a - b)  // Numerical sort
      if (sums.indexOf(Number(line)) === -1) {
        return line
      }
    }
  }
  return -1  // Hoping this line is not reached but makes strict TS happy.
}


function part2(data: number[], target: number): number {
  let min: number = 0
  let max: number = 1
  while (max < data.length) {
    let values: number[] = data.slice(min, max)
    let sum = values.reduce((total, x) => total + x) // Non-ES6 way.
    let sum = Math.sum(...values)
    if (sum === target) {
       return Math.min(...values) + Math.max(...values)
    } else if (sum < target) {
       max += 1
    } else {
      min += 1
    }
  }
  return -1  // Hoping this line is not reached but makes strict TS happy.
}


let data: string[] = input.split('\n')
let numbers: number[] = data.map(line => Number(line))  // Convert str to numbers
let part1_result: number = part1(numbers)
console.log('Part1: ' + part1_result)
console.log('Part2: ' + part2(numbers, part1_result))
