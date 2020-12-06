#!/usr/bin/env python

import unittest
import day06


class TestDay(unittest.TestCase):
    def test_check_group(self):
        data = ['a', 'a', 'c', 'a', '']
        day06.part2(data)
        data = ['ab', 'bc', 'cd', 'ad']
        day06.part2(data)


if __name__ == '__main__':
    unittest.main()
