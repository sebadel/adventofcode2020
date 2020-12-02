# adventofcode2020
Advent Of Code 2020


## Day 02: Password policy check
### Part 1
No specific difficulty here

#### Part 2
I made one mistake considering the valdity of a password.
I only considered valid a password if the first check was True and the second one was False.
This actually was validated by my test suite.
I ended up with a wrong answer until I considered that another valid password could be mismatch on the first char and a match on the 2nd char.
