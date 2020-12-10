# adventofcode2020
Advent Of Code 2020

## Day 02: Password policy check
### Part 1
No specific difficulty here

### Part 2
I made one mistake considering the valdity of a password.
I only considered valid a password if the first check was True and the second one was False.
This actually was validated by my test suite.
I ended up with a wrong answer until I considered that another valid password could be mismatch on the first char and a match on the 2nd char.

## Day 03: Toboggan slope trajectory
### Part 1
 - Wasted time because I failed to strip the input data :(

### Part 2
 - Learned math.prod is only available in Python >= 3.8.
 - Forgot to start parsing the input from line == down_step. data[down_step:0] instead of data[1:].

## Day 04: Passport validation
### Part 1
 - Did not process the last passport because it was triggered by empty lines; first answer submission was short by 1 :(

 ### Part 2
  - Tried to validate in one single if statement but couldn't debug.
  - Broke down the vailidation tests in functions and unit tested them. 
  - Careful with range: 5 is not in range(0,5), it is in range(0,6).
  - Improved my regexp skills - trying to capture groups but doing one single eval.
  - Discovered a Python 3.8 feature: the walrus operator.

## Day 05: Finding a seat on the plane
### Part 1
 - I didn't realize directly the analogy with binary representation.

### Part 2
 - Lost time trying to optimize with lambda or itertools.
 - I still believe there must be an elegant set comparison that can compare "neighbor" seats.

## Day 06: Passenger customs form
### Part 1
 - Need to find a better way to turn a str to a set of chars.

### Part 2
 - Need to find a better way to initialize the set at first line of the group.

## Day 07: Luggage check
### Part 1
 - I was wondering when recusrsion was going to start ?

### Part 2
 - I shouldn't have assumed that 'gold' was a sufficient filter, 'shiny gold' was necessary since other types of gold were in the list of colors.


## Day 08: Handheld instruction set
### Part 1
 - Got bitten by empty lines at the end of the input file.

### Part 2
 - Found an iterative way to get to the solution.
 - Can't find a working recursive methodology :(

### Part 2b
  - I really wanted to improve the solution with a recursive function; I couldn't do it without deep copying the instruction set - which is probably not very efficient.

## Day 09: Protocol decryption
### Part 1
 - Had to isolate pair in a function - wish I could do without the nested loop.

### Part 2
 - too many off-by-one notations but works OK. 

## Day 10: Adapter mess
### Part 1
 - Not elegant but not complex.
 - Took a little while to figure out what the problem exactly was.
 - Found out it only takes one unknown word (jolt) to make a problem much harder to grasp.

### Part 2 
- I won't lie, I suffered ... but the satisfaction is proportional
- The testing of the puzzle use case was succesful but the solving of my input took hours to execute ... 
- First you think it might take a few mins so my_lazy_and_confident_self is satisfied and just keeps an eye on the laptop
So here is what my morning was like:
Tested the part2 on the demo input, yeah, it works, run it with the real puzzle input ... hmmm, slower, but my_lazy_and_super_confident_self knows it is a matter of seconds or maybe even a few minutes...
- hmmm, still no output, let's go shower quickly, 
- hmmm, still no ouput, let's wake up the wife, 
- hmmm, still no output ... but 3% battery, run to find your laptop adapter, 
- hmmm, still no output ... prepare breakfast for the kids
- hmmm, still no output ... take the kids to school ... but don't ask me to smile
- really, 2 hours and still no output ... maybe I could start working on a more efficient solution ... 
- OK, time's up, it will be for tonight, let's get to work
- Oh, but wait, maybe ... I think ... if I did this ... it should ... let's try ... failed ... back to work for 10 min
- repeat until noon until it finally beautifully executed in 0.02sec




# Interesting links
## Utility from salt-die
https://github.com/salt-die/Advent-of-Code/blob/master/2020/aoc_helper
 - automated download of input
 - automated submission
 - automated template-based per-day directory creation