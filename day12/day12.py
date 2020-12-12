#!/usr/bin/env python


def manhattan_distance(position):
    return(
        abs(position['E'] - position['W']) +
        abs(position['S'] - position['N']))


def part1(data):
    position = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
    direction = 'E'
    for line in data:
        action, units = line[0], int(line[1:])
        if action in 'NESW':
            # Move in direction
            position[action] += units
        elif action == 'F':
            # Move forward
            position[direction] += units
        elif action in ['L', 'R']:
            # Change direction
            offset = units/90
            if action == 'L':
                offset = -offset
            direction = 'NESW'[('NESW'.index(direction) + offset) % 4]
    return manhattan_distance(position)


def part2(data):
    waypoint = {'N': 1, 'E': 10, 'S': 0, 'W': 0}
    position = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
    for line in data:
        action, units = line[0], int(line[1:])
        if action in 'NESW':
            # Move the waypoint
            waypoint[action] += units
        elif action == 'F':
            # Move the ship towards the waypoint.
            for direction, x in waypoint.items():
                position[direction] += units*x
        if action in ['L', 'R']:
            # Move the waypoint around the ship
            offset = units/90
            if action == 'L':
                offset = -offset
            new_waypoint = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
            for i in range(4):
                new_waypoint['NESW'[(i + offset) % 4]] = waypoint['NESW'[i]]
            waypoint = new_waypoint
    return manhattan_distance(position)


def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    print('Part 1: %s' % part1(data))
    print('Part 2: %s' % part2(data))


if __name__ == "__main__":
    main()
