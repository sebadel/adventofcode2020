#!/usr/bin/env python

import datetime


def part2(data, n):
    """
        memory = {x: [before_last_occurrence, last_occurrence]}
    """
    memory = Memory()
    for i, x in enumerate(data):
        memory.record(x, i+1)
    turn = len(data) + 1
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
                turn, memory.size,
                (datetime.datetime.now() - start).total_seconds()))
    return x


class Memory():
    def __init__(self):
        self.__divider = 100
        self._data = {}

    def get_data(self, x):
        div, mod = self._break_down_x(x)
        return self._data[div][mod]

    @property
    def size(self):
        _size = 0
        for x in self._data:
            for y in self._data[x]:
                _size += len(self._data[x][y])
        return _size

    def _break_down_x(self, x):
        return x // self.__divider , x % self.__divider

    def occurred_at_least_twice(self, x):
        try:
            occurrences = self.get_data(x)
            return (occurrences[-2], occurrences[-1])
        except IndexError:
            return False

    def record(self, x, turn):
        div, mod = self._break_down_x(x)
        try:
            self._data[div][mod].append(turn)
        except KeyError:
            try:
                self._data[div][mod] = [turn]
            except KeyError:
                self._data[div] = {mod: [turn]}


def main():
    data = [int(x) for x in '15,5,1,4,7,0'.split(',')]
    print('Part 2: %s' % part2(data, 30000000))


if __name__ == "__main__":
    main()
