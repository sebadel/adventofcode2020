#!/usr/bin/env python

import datetime


def part2(data, n):
    """
        memory = {x: [before_last_occurrence, last_occurrence]}
    """
    memory = Memory()
    for i, x in enumerate(data):
        memory.record(x, i+1)
    turn = memory.next_turn
    max_turns = n
    x = data[-1]
    start = datetime.datetime.now()
    while turn <= max_turns:
        occ = memory.occurred_at_least_twice(x)
        if occ:  # occurred at least twice
            x = occ[1] - occ[0]
        else:  # Didn't occur at least twice.
            x = 0
        memory.record(x, turn)
        turn += 1
        # Optional counter - probably slows down the process a little bit.
        if turn in [100000, 1000000, 10000000, 20000000, 30000000]:
            print ('Turn: %s - memory: %d - execution time: %s s' % (
                turn, len(memory.data),
                (datetime.datetime.now() - start).total_seconds()))
    return x


class Memory():
    def __init__(self):
        self.data = {}

    @property
    def next_turn(self):
        return len(self.data) + 1

    @property
    def last(self):
        return self.data[-1]

    def occurred_at_least_twice(self, x):
        try:
            occurrences = self.data[x]
            return (occurrences[-2], occurrences[-1])
        except IndexError:
            return False

    def record(self, x, turn):
        try:
            self.data[x].append(turn)
        except KeyError:
            self.data[x] = [turn]


def main():
    data = [int(x) for x in '15,5,1,4,7,0'.split(',')]
    print('Part 2: %s' % part2(data, 30000000))


if __name__ == "__main__":
    main()
