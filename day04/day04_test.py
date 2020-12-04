#!/usr/bin/env python

import unittest
import day04


class TestPart2(unittest.TestCase):
    def test_check_size(self):
        self.assertFalse(day04.check_size('149cm'))
        self.assertTrue(day04.check_size('150cm'))
        self.assertTrue(day04.check_size('151cm'))
        self.assertTrue(day04.check_size('193cm'))
        self.assertFalse(day04.check_size('151in'))

    def test_check_hcl(self):
        self.assertTrue(day04.check_hcl('#1234ab'))
        self.assertTrue(day04.check_hcl('#123456'))
        self.assertFalse(day04.check_hcl('#1234567'))
        self.assertFalse(day04.check_hcl('#a234567'))

    def test_check_ecl(self):

if __name__ == '__main__':
    unittest.main()