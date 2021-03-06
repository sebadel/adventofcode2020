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

## Day 11: Seat allocation
No particular comment, just couldn't find time to finish it
in the morning.

## Day 12: Seat allocation
### Part2
Not fully satisfied with the direction shifting, there probably are more arithmetic ways to store waypoint and position coordinates.

## Day 13: Bus schedules
### Part1
- No particular difficulty

### Part2
- I struggled hard - after multiple hours of not finding, I finally went to subreddit and used a solution for inspiration
- My solution actually worked but way too slow - I kept on bruteforcing with a constant increase (equal to max(buses).
- The main limitation was that I could not find how to increase the step.
- It turned out the right way is to compare 2 buses, then go to the next one by multiplying the increase by the value of the new bus.
- Another hint was to ignore the 'x' values by replacing them with 0 instead of keeping a dict with {offset: bus}.
- Interesting read about the Chinese Remainder Theory (https://en.wikipedia.org/wiki/Chinese_remainder_theorem).

# Day 14: Docking data and bitwise operations
## Part 1:
 - Refreshing reminder about bitwise operations.

## Part 2:
 - Nothing particular

# Day 15: Memory game with the elves
## Part 1:
 - No particular difficulty

## Part2:
 - Took ~1.5h to reach acceptable performance (execution time: 57sec).
 - Interesting to notice that removing the counter (n 'if' statement) didn't reduce the execution speed.
 - Trimmed 2 secs by using IndexErrors instead of testing index validity: ~55sec.
 - Trimmed 2 secs by using Python 3.6.8 instead of Python 2.7.16.
 - No impact when using a list instead of a dict to hold the numbers.
 - ~39sec using a Memory class (day15b.py)

# Day 16:
## Part 1:
 - As usual, pretty straightforward

## Part 2:
 - Quickly came to the solution but it took a serious amount of troubleshooting to understand a function was
 returning an int or None if not found; later on, this value was tested with "if value:".
The side effect of this is that this became False if the function returned an index of 0 :(((
 - On to day 17 now, personal record broken at this point ;)

# Day 17:
## Part 1:
 - This one took some time to understand the best way to model it.

## Part 2:
 - Once P1 was done, this one was 8 mins.

# Day 18:
## Part 1:
 - Completed on time but needs some refactoring before I share on GitHub

## Part 2:
 - Completed on time but needs some refactoring before I share on GitHub

# Day 19:
## Part 1:
 - Spent more time on Strava than on AoC ;)
 - Needs to catch up with the backlog

## Part 2:
 - [2020/12/27] Finally wrapped my head around this one. Got a hint from a friend, and gave up the elegant solution for the bruteforce "capped recursivity" - Not 100% satisfied but moving on ;)


# Day 20:
## Part 1:
 - Got one silver star for day 20 on day 20

## Part 2:
 - Overlooked the instruction to remove the border from the tiles :((

# Day 21:
## Part 1
  - Haven't opened the problem on day 21.
  - Hoping to get 19 and 20 finished by tomorrow (22) and get to 21 after tomorrow (23)
  - From rank #40 to #rank 60 on [Matt Goodrich's leaderboard](https://adventofcode.com/2020/leaderboard/private/view/411675)
  - [2020/12/28] Got inspiration from https://github.com/UnicycleBloke/aoc2020/blob/main/day21/day21.py abut the right use of sets.

 ## Part 2:
  - Not the cleanest way but good enough for today.
  - Read extensively about the usage of argument splitting.

# Day 22:
## Part 1:
  - First time usage of queue.Queue() - working as intended ;)

## Part 2:

# Day 23:
## Part 1:
 - No major issue

## Part 2:
 - Part 1 did not scale with larger numbers
 - Changed the array structure to a chain of pointers (nostalgic flashback from CS classes in '96)
 - Works sub 25 sec, which is OK

# Day 24:
## Part 1:
 - First time using an hex grid, proud to have found a working solution without external inspiration.
 - No major issue

## Part 2:
 - I failed to understand I needed to make the grid bigger (by 2 units in each direction) at every turn. I still think it was not clear in the problem description.
 - Oooh, and we are the 19th of Feb, I missed the end of year deadline, procrastinated for 50 days now but I'm not giving up ;)



# Interesting links
## Utility from salt-die
https://github.com/norvig/pytudes/blob/master/ipynb/Advent-2020.ipynb
 - nice resources around Python optimisation

https://github.com/salt-die/Advent-of-Code/blob/master/2020/aoc_helper
 - automated download of input
 - automated submission
 - automated template-based per-day directory creation