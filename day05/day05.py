#!/usr/bin/env python


def row(x):
    x = x[0:7]
    x = x.replace('F', '0').replace('B', '1')
    return int(x, 2)


def seat(x):
    x = x[7:10]
    x = x.replace('L', '0').replace('R', '1')
    return int(x, 2)


def part1(data):
    seats = [row(line) * 8 + seat(line) for line in data]
    return max(seats)


def part2(data):
    tickets = [row(line) * 8 + seat(line) for line in data]
    plane_seats = list(range(0, 128*8))
    missing_seats = set(plane_seats) - set(tickets)
    for i in missing_seats:
        if i-1 not in missing_seats and i+1 not in missing_seats:
            return i


def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    print('Part 1: %d' % part1(data))
    print('Part 2: %d' % part2(data))


if __name__ == "__main__":
    main()
