#!/usr/bin/env python

import unittest
import day12


class TestDay12(unittest.TestCase):
    def test_part1(self):
        self.data = ['F10', 'N3', 'F7', 'R90', 'F11']
        self.assertEqual(25, day12.part1(self.data))

    def test_rotation(self):
        self.data = ['R180', 'F5']
        self.assertEqual(5, day12.part1(self.data))


if __name__ == '__main__':
    unittest.main()
