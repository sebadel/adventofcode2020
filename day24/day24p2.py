#!/usr/bin/env python

import copy
BLACK = True
WHITE = False


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


def get_position(directions, x=0, y=0):
    for d in directions:
        if 'n' in d:
            y += 2 / len(d)
        if 's' in d:
            y -= 2 / len(d)
        if 'e' in d:
            x += 2 / len(d)
        if 'w' in d:
            x -= 2 / len(d)
    return (x, y)


def cnt_black_neighbors(tiles, position):
    cnt = 0
    directions = ['e', 'se', 'sw', 'w', 'nw', 'ne']
    for d in directions:
        p = get_position([d], position[0], position[1])
        if p in tiles and tiles[p] == BLACK:
            cnt += 1
    return cnt


def apply_day_rules(tiles):
    t = copy.copy(tiles)
    for position, tile in tiles.items():
        if (tile == BLACK and
                cnt_black_neighbors(tiles, position) not in [1, 2]):
            t[position] = WHITE
        if tile == WHITE and cnt_black_neighbors(tiles, position) == 2:
            t[position] = BLACK
    return t


def fill_grid(tiles):
    min_x = int(min([t[0] for t in tiles]))
    max_x = int(max([t[0] for t in tiles]))
    min_y = int(min([t[1] for t in tiles]))
    max_y = int(max([t[1] for t in tiles]))
    for x in range(min_x-2, max_x+2):
        for y in range(min_y-2, max_y+2):
            if (x, y) not in tiles:
                tiles[(x, y)] = WHITE


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
    day = 0
    while day < days:
        day += 1
        fill_grid(tiles)
        tiles = apply_day_rules(tiles)
        print('[Day %d] %d black tiles / %d tiles' % (
            day,
            len([v for v in tiles.values() if v == BLACK]),
            len(tiles)
        ))
    return len([v for v in tiles.values() if v == BLACK])


def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    print('Part 2: %s' % part2(data))


if __name__ == "__main__":
    main()
