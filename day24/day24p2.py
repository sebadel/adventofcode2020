#!/usr/bin/env python

def parse_line(line):
    directions = []
    while(line):
        if line[0] == 'n' or line[0] == 's':
            directions.append(line[0:2])
            line = line[2:]
        else:
            directions.append(line[0:1])
            line = line[1:]
    return directions


def get_position(directions):
    x = 0
    y = 0
    for d in directions:
        if 'n' in d:
            y += 1 / len(d)
        if 's' in d:
            y -= 1 / len(d)
        if 'e' in d:
            x += 1 / len(d)
        if 'w' in d:
            x -= 1 / len(d)
    return (x, y)


def apply_day_rules(tiles):


def part2(data, days=100):
    BLACK = True
    WHITE = False

    tiles = {}
    for line in data:
        directions = parse_line(line)
        tile_position = get_position(directions)
        if tile_position not in tiles:
            tiles[tile_position] = WHITE
        tiles[tile_position] = not tiles[tile_position]
        print('[%s] [%s] [%d/%d]' % (
            directions,
            tile_position,
            len([v for v in tiles.values() if v == BLACK]),
            len(tiles)
        ))
    day = 0
    while day < days:
        day += 1
        apply_day_rules(tiles)
    return len([v for v in tiles.values() if v == BLACK])

def

def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    print('Part 1: %s' % part1(data))


if __name__ == "__main__":
    main()
