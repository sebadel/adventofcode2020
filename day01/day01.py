#!/usr/bin/env python

from typing import Union, List


def part1(data):
    while len(data) > 0:
        a = data.pop()
        x = 2020-a
        if x in data:
            print('%d * %d = %d' % (a, x, a*x))


def find_pair(data: List[int], target: int) -> Union[List[int], bool]:
    for a in data:
        x = target - a
        if x in data:
            print('\t %d + %d' % (a, x))
            print('%d * %d = %d' % (a, x, a*x))
            return [a, x]
    return False


def part2(data: List[int], target: int = 2020):
    while len(data) > 0:
        a = data.pop()
        print(a)
        pair = find_pair(data, target - a)
        if pair:
            print('%d * %d * %d = %d' % (
                a, pair[0], pair[1], a*pair[0]*pair[1]))
            return True


def main():
    data = open('input.txt', 'r').readlines()
    data = [int(x) for x in data]
    part1(data)
    data = open('input.txt', 'r').readlines()
    data = [int(x) for x in data]
    part2(data)


main()
