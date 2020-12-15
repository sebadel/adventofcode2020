#!/usr/bin/env python

import datetime


def part1(data, n):
    i = 0
    spoken = []
    while i < n:
        if i < len(data):
            spoken.append(data[i])
        else:
            last_number = spoken[-1]
            if last_number not in spoken[:-1]:
                spoken.append(0)
            else:
                found = False
                search_i = len(spoken) - 2
                while search_i >= 0 and not found:
                    if spoken[search_i] == last_number:
                        spoken.append(len(spoken) - search_i-1)
                        found = True
                    search_i -= 1
        i += 1
    return spoken[-1]


def part2(data, n):
    """
        last_spoken = {x: [iterations, last]}
    """
    memory = {}
    for i, x in enumerate(data):
        record_number(memory, x, i+1)
    turn = len(data) + 1
    max_turns = n
    x = data[-1]
    start = datetime.datetime.now()
    while turn <= max_turns:
        if x in memory and not memory[x][0]:  # Occurred before but only once.
            x = 0
        else:  # Never occurred before or occurred multiple times
            x = memory[x][1] - memory[x][0]
        record_number(memory, x, turn)
        turn += 1
        # Optional counter - probably slows down the process a little bit.
        if turn in [100000, 1000000, 10000000, 20000000, 30000000]:
            print ('%s: %s s' % (
                turn, (datetime.datetime.now() - start).total_seconds()))
    return x


def record_number(memory, n, turn):
    """Records the 2 last occurrence (turns) of n."""
    if n not in memory:
        memory[n] = (None, turn)
    else:
        memory[n] = (memory[n][1], turn)


def main():
    data = [int(x) for x in '15,5,1,4,7,0'.split(',')]
    print('Part 1: %s' % part1(data, 2020))
    print('Part 2: %s' % part2(data, 30000000))


if __name__ == "__main__":
    main()
