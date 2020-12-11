#!/usr/bin/env python

import unittest
import day11


class TestDay11Part1(unittest.TestCase):
    def setUp(self):
        self.data1 = [
            'L.LL.LL.LL',
            'LLLLLLL.LL',
            'L.L.L..L..',
            'LLLL.LL.LL',
            'L.LL.LL.LL',
            'L.LLLLL.LL',
            '..L.L.....',
            'LLLLLLLLLL',
            'L.LLLLLL.L',
            'L.LLLLL.LL'
        ]

#    def test_check_seat(self):
#        self.assertEqual('L', day11.check_seat(self.data1, [0, 0]))
#        self.assertEqual('#', day11.check_seat(self.data1, [1, 0]))
#        self.assertEqual('#', day11.check_seat(self.data1, [-4, 34]))

    def test_change_seat(self):
        day11.change_seat(self.data1, [0, 0])
        self.assertEqual('#', day11.check_seat(self.data1, [0, 0]))

    def test_part1(self):
        day11.part1(self.data1)
#        self.assertEqual('#', day11.check_seat(self.data1, [0, 0]))


class TestDay11Part2(unittest.TestCase):
    def setUp(self):
        self.data1 = [
            '.......#.',
            '...#.....',
            '.#.......',
            '.........',
            '..#L....#',
            '....#....',
            '.........',
            '#........',
            '...#.....',
        ]
        self.data2 = [
            '.............',
            '.L.L.#.#.#.#.',
            '.............'
        ]
        self.data3 = [
            '.##.##.',
            '#.#.#.#',
            '##...##',
            '...L...',
            '##...##',
            '#.#.#.#',
            '.##.##.'
        ]

    def test_visible_seat_states(self):
        self.assertEqual('L', day11.check_seat(self.data1, [3, 4]))
        neighbors = day11.visible_seat_states(self.data1, 3, 4)
        print(neighbors)
        self.assertEqual(8, neighbors.count('#'))

        self.assertEqual('L', day11.check_seat(self.data2, [1, 1]))
        neighbors = day11.visible_seat_states(self.data2, 1, 1)
        print(neighbors)
        self.assertEqual(1, neighbors.count('L'))

        self.assertEqual('L', day11.check_seat(self.data3, [3, 3]))
        neighbors = day11.visible_seat_states(self.data3, 3, 3)
        print(neighbors)
        self.assertEqual(0, neighbors.count('#'))


if __name__ == '__main__':
    unittest.main()
