#!/usr/bin/env python

import day20


def ordered_tiles(matrix):
    tiles = []
    for y in range(matrix.min_y, matrix.max_y + 1):
        for x in range(matrix.min_x, matrix.max_x + 1):
            tiles.append(matrix.get_tile_by_xy(x, y))
    return tiles


def is_monster(zone, monster):
    """Does the zone (3x20 chars) match a monster pattern ? """
    monster_matches = set(
        [i for i, ltr in enumerate(monster) if ltr == '#'])
    zone_matches = set(
        [i for i, ltr in enumerate(zone) if ltr == '#'])
    return monster_matches.issubset(zone_matches)


def remove_tile_border(data):
    return [row[1:-1] for row in data[1:-1]]


class SeaMonsterMatrix(object):
    def __init__(self, matrix_size, tile_size):
        self.matrix_size = matrix_size
        self.tile_size = tile_size
        size = matrix_size * tile_size
        self.data = [[' ' for col in range(size)] for row in range(size)]

    def LoadFromTiles(self, tiles):
        for t, tile in enumerate(tiles):
            for r, row in enumerate(tile):
                for c, char in enumerate(row):
                    x = (t % self.matrix_size) * self.tile_size + c
                    y = (t // self.matrix_size) * self.tile_size + r
                    self.data[y][x] = char

    def CountDash(self):
        return ''.join([''.join(x) for x in self.data]).count('#')

    def DetectMonsters(self):
        monster = ''.join([
            '                  # ',
            '#    ##    ##    ###',
            ' #  #  #  #  #  #   ',
        ])
        zone = ''
        count = 0
        m_size = int(len(monster)/3)
        for y, row in enumerate(self.data[:-2]):
            for x in range(0, 1 + len(row) - m_size):
                zone = ''.join([
                    ''.join(row[x:x+m_size]),
                    ''.join(self.data[y+1][x:x+m_size]),
                    ''.join(self.data[y+2][x:x+m_size])
                ])
                if is_monster(zone, monster):
                    print(zone, monster)
                    count += 1
        return count

    def flip_h(self):
        self.data = [x[::-1] for x in self.data]

    def flip_v(self):
        x = []
        for i in range(0, len(self.data)):
            x.append(self.data[len(self.data) - 1 - i])
        self.data = x

    def rotate90(self):
        x = []
        for i in range(0, len(self.data)):
            x.append(''.join([row[i] for row in self.data])[::-1])
        self.data = x


def part2(data):
    m = day20.part1(data, True)
    m2 = SeaMonsterMatrix(12, 8)
    m2.LoadFromTiles([remove_tile_border(t.data) for t in ordered_tiles(m)])
    nb_monsters = m2.DetectMonsters()
    HASHTAGS_IN_MONSTER = 15
    print('%d #\'s - %d monsters * %d = %d' % (
        m2.CountDash(), nb_monsters, HASHTAGS_IN_MONSTER,
        m2.CountDash() - (nb_monsters * 15)))
    OPERATIONS = [
        'rotate90', 'rotate90', 'rotate90', 'rotate90',
        'flip_h', 'rotate90', 'rotate90', 'rotate90', 'rotate90', 'flip_h',
        'flip_v', 'rotate90', 'rotate90', 'rotate90', 'rotate90', 'flip_v',
        'flip_h', 'flip_v', 'rotate90', 'rotate90', 'rotate90', 'rotate90'
    ]
    for op in OPERATIONS:
        getattr(m2, op)()
        print('%d #\'s - %d monsters * %d = %d' % (
            m2.CountDash(), nb_monsters, HASHTAGS_IN_MONSTER,
            m2.CountDash() - (nb_monsters * 15)))


def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
#    print('Part 1: %s' % part1(data))
    print('Part 2: %s' % part2(data))


if __name__ == "__main__":
    main()
