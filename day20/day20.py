#!/usr/bin/env python

import math


class Matrix(object):
    def __init__(self):
        self.tiles = []  # [Tile(), ...]
        self.positions = set()  # [(x, y, id), (), ...]
        self.x = 0
        self.y = 0

    def fit(self, x, y, tile):
        """Tries to fit a tile in the grid."""
        if (
            (not self.get_tile_by_xy(x, y-1) or
             tile.top_edge == self.get_tile_by_xy(x, y-1).bottom_edge) and
            (not self.get_tile_by_xy(x, y+1) or
             tile.bottom_edge == self.get_tile_by_xy(x, y+1).top_edge) and
            (not self.get_tile_by_xy(x-1, y) or
             tile.left_edge == self.get_tile_by_xy(x-1, y).right_edge) and
            (not self.get_tile_by_xy(x+1, y) or
             tile.right_edge == self.get_tile_by_xy(x+1, y).left_edge)
        ):
            self.position_tile(x, y, tile)
            return True
        else:
            return False

    @property
    def gaps(self):
        """Positions that are currently not filed with a tile."""
        g = []
        for x, y, id in self.positions:
            for xx, yy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if not self.get_tile_by_xy(xx, yy):
                    g.append((xx, yy))
        return list(set(g))

    @property
    def sorted_gaps(self):
        """Sorting the gaps.
           Preferring the ones to closer to the center of the matrix.
        """
        gaps = self.gaps
        gaps.sort(key=lambda x: abs(x[0]) - abs(x[1]))
        return gaps

    @property
    def min_x(self):
        return min([p[0] for p in self.positions])

    @property
    def max_x(self):
        return max([p[0] for p in self.positions])

    @property
    def min_y(self):
        return min([p[1] for p in self.positions])

    @property
    def max_y(self):
        return max([p[1] for p in self.positions])

    def position_tile(self, x, y, tile):
        self.positions.add((x, y, tile.name))

    def get_tile_by_xy(self, x, y):
        for p in self.positions:
            if p[0] == x and p[1] == y:
                tt = [t for t in self.tiles if t.name == p[2]]
                if tt:
                    return tt[0]
        return None

    @property
    def unpositioned_tiles(self):
        ut = []
        for t in self.tiles:
            if t.name not in [p[2] for p in self.positions]:
                ut.append(t)
        return ut

    def display(self):
        for y in range(self.min_y, self.max_y + 1):
            for x in range(self.min_x, self.max_x + 1):
                tile = self.get_tile_by_xy(x, y)
                if tile:
                    print('%5s' % tile.name, end=' ')
                else:
                    print('  -  ', end=' ')
            print()


class Tile(object):
    def __init__(self, name, data):
        self.name = name.strip()
        self.data = data

    def flip_h(self):
        """Horizontal flip."""
        self.data = [x[::-1] for x in self.data]

    def flip_v(self):
        """Vertical flip."""
        x = []
        for i in range(0, len(self.data)):
            x.append(self.data[len(self.data) - 1 - i])
        self.data = x

    def rotate90(self):
        x = []
        for i in range(0, len(self.data)):
            x.append(''.join([row[i] for row in self.data])[::-1])
        self.data = x

    @property
    def top_edge(self):
        return self.data[0]

    @property
    def bottom_edge(self):
        return self.data[-1]

    @property
    def left_edge(self):
        return ''.join([x[0] for x in self.data])

    @property
    def right_edge(self):
        return ''.join([x[-1] for x in self.data])


def part1(data, return_matrix=False):
    m = Matrix()
    lines = '\n'.join(data)
    tile_strs = lines.split('\n\n')
    for tile_str in tile_strs:
        tile_data = tile_str.split('\n')
        tile = Tile(tile_data[0].split(' ')[1].strip(':'), tile_data[1:])
        m.tiles.append(tile)

    m.position_tile(0, 0, m.tiles[0])
    OPERATIONS = [
        'rotate90', 'rotate90', 'rotate90', 'rotate90',
        'flip_h', 'rotate90', 'rotate90', 'rotate90', 'rotate90', 'flip_h',
        'flip_v', 'rotate90', 'rotate90', 'rotate90', 'rotate90', 'flip_v',
        'flip_h', 'flip_v', 'rotate90', 'rotate90', 'rotate90', 'rotate90'
    ]
    while m.unpositioned_tiles:
        for gap in m.sorted_gaps:
            for tile in m.unpositioned_tiles:
                if not m.fit(gap[0], gap[1], tile):
                    for operation in OPERATIONS:
                        getattr(tile, operation)()
                        if m.fit(gap[0], gap[1], tile):
                            break
        print('%d  positioned / %d' % (
            len(m.positions), len(m.tiles)))
        m.display()
    if return_matrix:
        return m
    return (
        int(m.get_tile_by_xy(m.min_x, m.min_y).name) *
        int(m.get_tile_by_xy(m.min_x, m.max_y).name) *
        int(m.get_tile_by_xy(m.max_x, m.min_y).name) *
        int(m.get_tile_by_xy(m.max_x, m.max_y).name)
    )


def part2(data):
    pass


def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    print('Part 1: %s' % part1(data))
    print('Part 2: %s' % part2(data))


if __name__ == "__main__":
    main()
