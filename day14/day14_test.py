#!/usr/bin/env python

import unittest
import day14


class TestDay14(unittest.TestCase):
    def test_validity(self):
        pass

    def test_expand(self):
#        print(day14.expand('0101X0X1'))
        num = 42
        print(format(num, '036b'))
        mask = '000000000000000000000000000000X1001X'
        print(mask)
        result = day14.apply_mask2(format(num, '036b'), mask)
        print(result)
        print(day14.expand(result))


if __name__ == '__main__':
    unittest.main()
