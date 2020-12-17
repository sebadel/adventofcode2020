#!/usr/bin/env python

import copy


def _str(x, y, z, w):
    return '|'.join([str(x), str(y), str(z), str(w)])


def _xyzw(s):
    return [int(x) for x in s.split('|')]


class Pocket(object):
    def __init__(self,):
        self._cubes = set()
        self.min_x = -1
        self.max_x = 3
        self.min_y = -1
        self.max_y = 3
        self.min_z = -1
        self.max_z = 3
        self.min_w = -1
        self.max_w = 3
        self._sshot = None

    def snapshot(self):
        self._sshot = copy.copy(self._cubes)

    @property
    def cubes(self):
        c = []
        for w in range(self.min_w - 1, self.max_w + 2):
            for z in range(self.min_z - 1, self.max_z + 2):
                for y in range(self.min_y - 1, self.max_y + 2):
                    for x in range(self.min_x - 1, self.max_x + 2):
                        c.append(_str(x, y, z, w))
        return c

    def adjust_size(self, xyzw):
        x, y, z, w = _xyzw(xyzw)
        self.min_x = min(x, self.min_x)
        self.max_x = max(x, self.max_x)
        self.min_y = min(y, self.min_y)
        self.max_y = max(y, self.max_y)
        self.min_z = min(z, self.min_z)
        self.max_z = max(z, self.max_z)
        self.min_w = min(w, self.min_w)
        self.max_w = max(w, self.max_w)

    def set_cube(self, xyzw, state):
        if state == '#':
            self._cubes.add(xyzw)
        else:
            if xyzw in self._cubes:
                self._cubes.remove(xyzw)
        self.adjust_size(xyzw)

    def get_cube(self, xyzw, from_snapshot=False):
        if from_snapshot:
            if xyzw in self._sshot:
                return '#'
            else:
                return '.'
        if xyzw in self._cubes:
            return '#'
        return '.'

    @property
    def active_cubes(self):
        return self._cubes

    def neighbors(self, xyzw):
        n = []
        x, y, z, w = _xyzw(xyzw)
        for ww in range(w - 1, w + 2):
            for zz in range(z - 1, z + 2):
                for yy in range(y - 1, y + 2):
                    for xx in range(x - 1, x + 2):
                        coords = _str(xx, yy, zz, ww)
                        if coords != xyzw:
                            n.append(coords)
        return n

    def active_neighbors(self, xyzw, from_snapshot=False):
        an = set()
        for n in self.neighbors(xyzw):
            if from_snapshot:
                if n in self._sshot:
                    an.add(n)
            else:
                if n in self._cubes:
                    an.add(n)
        return an


def part2(data, turns=6):
    p = Pocket()
    for y, row in enumerate(data):
        for x, state in enumerate(row):
            p.set_cube(_str(x, y, 0, 0), state)
    i = 0
    while i < turns:
        p.snapshot()
        for xyzw in p.cubes:
            if p.get_cube(xyzw, from_snapshot=True) == '#':
                if len(p.active_neighbors(xyzw, from_snapshot=True)) in [2, 3]:
                    p.set_cube(xyzw, '#')
                else:
                    p.set_cube(xyzw, '.')
            else:
                if len(p.active_neighbors(xyzw, from_snapshot=True)) == 3:
                    p.set_cube(xyzw, '#')
        i += 1
    return len(p.active_cubes)


def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    print('Part 2: %s' % part2(data))


if __name__ == "__main__":
    main()
