#!/usr/bin/env python


def part1(data):
    x = 0
    cnt = 0
    for line in data[1:]:
        x += 3
        x = x % len(line)
        if line[x] == '#':
            cnt += 1
    return cnt


def part2(data):
    simulations = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]
    total = 1
    for s in simulations:
        total = total * _part2(data, s[0], s[1])
    return total


def _part2(data, right_step, down_step):
    x = 0
    cnt = 0
    for line_number, line in enumerate(data[down_step:]):
        if line_number % down_step != 0:
            continue
        x += right_step
        x = x % len(line)
        if line[x] == '#':
            cnt += 1
    return cnt


def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    print('Part 1: %d' % part1(data))
    print('Part 2: %d' % part2(data))


if __name__ == "__main__":
    main()
