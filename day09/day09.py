#!/usr/bin/env python


def pairs(data, cursor):
    """Returns sum of 24 previous numbers."""
    p = []
    for i in data[cursor-25:cursor]:
        for j in data[cursor-25:cursor]:
            p.append(i+j)
    return p


def part1(data):
    for cursor, x in enumerate(data):
        if cursor > 24:
            if x not in pairs(data, cursor):
                return x


def part2(data, x):
    low = 0
    high = 0
    while high <= len(data) - 1:
        s = sum(data[low:high + 1])
        if s < x:
            high += 1
        if s > x:
            low += 1
        if s == x:
            return(min(data[low:high+1]) + max(data[low:high+1]))


def main():
    data = [int(line.strip()) for line in open('input.txt', 'r').readlines()]
    part1_result = part1(data)
    print('Part 1: %s' % part1_result)
    print('Part 2: %s' % part2(data, part1_result))


if __name__ == "__main__":
    main()
