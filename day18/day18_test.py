#!/usr/bin/env python

import unittest
import day18


import re


class TestDay18(unittest.TestCase):
    def test_strip_whitespaces(self):
        x = '1 + (2 * 3) + (4 *   (5 + 6))'
        self.assertEqual('1+(2*3)+(4*(5+6))', re.sub(' ', '', x))
        x = '1 + (2 * 3) + (4 *   (5 + 6))'
        x = x.replace(' ', '')
        self.assertEqual('1+(2*3)+(4*(5+6))', x)

    def test_parenthesis(self):
        RE_INNER_PARENTHESIS = re.compile(r'\(([^()]*)\)')
        x = '1 + (2 * 3) + (4 * (5 + 6))'
        self.assertCountEqual(['2 * 3', '5 + 6'], RE_INNER_PARENTHESIS.findall(x))

    def test_replace_parenthesis(self):
        def _print(c):
            print(' -- %s -- ' % c)
            return eval(c)
        RE_INNER_PARENTHESIS = re.compile(r'\(([^()]*)\)')
        x = '(1 * (3 + 3)) + 2 + (2 + 6) + 1'.replace(' ', '')
        def func(v):
            return v.replace('2', '0')
        self.assertEqual('1+3*3+0+6+1',
            RE_INNER_PARENTHESIS.sub(lambda a: func(a.groups()[0]), x))

#    def test_evaluate(self):
#        self.assertEqual(10, day18.test('1+2+3+ 4'))
        self.assertEqual('23340', day18.test('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'))



if __name__ == '__main__':
    unittest.main()
