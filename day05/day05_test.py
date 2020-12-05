#!/usr/bin/env python

import unittest
import day05


class TestDay05(unittest.TestCase):
    def test_row(self):
        self.assertEqual(128,  day05.row('BBBBBBB'))
        self.assertEqual(65,  day05.row('BFFFFFF'))
        self.assertEqual(66,  day05.row('BFFFFFB'))

    def test_seat(self):
        self.assertEqual('A',  day05.seat('BBBBBBBLLL'))
        self.assertEqual('C',  day05.seat('BBBBBBBLRL'))
        self.assertEqual('F',  day05.seat('BBBBBBBRRR'))


if __name__ == '__main__':
    unittest.main()
