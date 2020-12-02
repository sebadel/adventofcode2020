#!/usr/bin/env python

import unittest
import day02


class TestPasswordLine(unittest.TestCase):
    def test_validity(self):
        self.assertTrue(day02.PasswordLine('1-3 a: abcde').valid())
        self.assertFalse(day02.PasswordLine('1-3 b: cdefg').valid())
        self.assertTrue(day02.PasswordLine('2-9 c: ccccccccc').valid())

    def test_validity_part2(self):
        self.assertTrue(day02.PasswordLine('1-3 a: abcde').valid_part2())
        self.assertFalse(day02.PasswordLine('1-3 b: cdefg').valid_part2())
        self.assertFalse(day02.PasswordLine('2-9 c: ccccccccc').valid_part2())
    
    def test_validity_part2_first_not_match_and_second_match(self):
        self.assertTrue(day02.PasswordLine('1-3 a: cbade').valid_part2())


if __name__ == '__main__':
    unittest.main()