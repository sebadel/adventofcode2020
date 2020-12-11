#!/usr/bin/env python

import copy


def check_seat(seats, xy):
    x, y = xy
    if x < 0 or y < 0:
        return '-'
    try:
        return seats[y][x]
    except IndexError:
        return '-'


def change_seat(seats, xy):
    x, y = xy
    try:
        seat = seats[y][x]
        if seat == '#':
            row = list(seats[y])
            row[x] = 'L'
            seats[y] = ''.join(row)
        elif seat == 'L':
            row = list(seats[y])
            row[x] = '#'
            seats[y] = ''.join(row)
        return True
    except IndexError:
        return False


def nb_occupied(seats):
    cnt = 0
    for row in seats:
        cnt += row.count('#')
    return cnt


def adjacent_seats(x, y):
    """Returns list of coords."""
    return [
        [x-1, y-1], [x, y-1], [x+1, y-1],
        [x-1, y],             [x+1, y],
        [x-1, y+1], [x, y+1], [x+1, y+1],
    ]


def check_visible_seat(seats, x, y, dx, dy):
    """Returns one seat state."""
    keep_looking = True
    while keep_looking:
        x += dx
        y += dy
        keep_looking = check_seat(seats, [x, y]) in ['.']
    return check_seat(seats, [x, y])


def visible_seat_states(seats, x, y):
    """Returns list of states."""
    directions = [
        [-1, -1], [0, -1], [+1, -1],
        [-1,  0],         [+1,  0],
        [-1, +1], [0, +1], [+1, +1],
    ]
    for i, pos in enumerate(directions):
        directions[i] = check_visible_seat(
            seats, x, y, pos[0], pos[1])
    return directions


def part1(seats):
    seats_copy = copy.deepcopy(seats)
    for y, row in enumerate(seats):
        for x, seat in enumerate(row):
            adj = adjacent_seats(x, y)
            neighbor_states = [check_seat(seats_copy, s) for s in adj]
            if seat == 'L' and '#' not in neighbor_states:
                change_seat(seats, [x, y])
            elif seat == '#' and neighbor_states.count('#') > 3:
                change_seat(seats, [x, y])
    if seats == seats_copy:
        nb = nb_occupied(seats)
        print('OK %d' % nb)
        return nb
    else:
        part1(seats)


def part2(seats):
    seats_copy = copy.deepcopy(seats)
    for y, row in enumerate(seats):
        for x, seat in enumerate(row):
            neighbor_states = visible_seat_states(seats_copy, x, y)
            if seat == 'L' and '#' not in neighbor_states:
                change_seat(seats, [x, y])
            elif seat == '#' and neighbor_states.count('#') > 4:
                change_seat(seats, [x, y])
    if seats == seats_copy:
        return nb_occupied(seats)
    part2(seats)


def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    nb = part1(data)
    print('Part 1: %d' % nb)
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    print('Part 2: %d' % part2(data))


if __name__ == "__main__":
    main()
