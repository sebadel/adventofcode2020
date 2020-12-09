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
