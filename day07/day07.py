#!/usr/bin/env python

import re


def rule_parser(rule):
    """Returns Tuple[str, List[str]]."""
    rule = re.sub(r'\sbags?', '', re.sub(r'\.', '', rule))
    bag, contents = rule.split(' contain ')
    contents = contents.split(', ')
    return (bag, contents)


def can_contain(colors, rules):
    bags = set()
    for parent, content in rules:
        for c in content:
            for color in colors:
                if color in c:
                    bags.add(parent)
    if bags:
        bags.update(can_contain(bags, rules))
    return bags


def what_is_in(color, rules):
    total = 1
    for parent, content in rules:
        if parent in color:
            for c in content:
                m = re.search(r'^(\d+)\s', c)
                if m:
                    n = int(m.groups()[0])
                    total = total + (n * what_is_in(c, rules))
    return total


def part1(data):
    """How many bags can contain at leaset 1 shiny gold bag?"""
    bags = can_contain(['shiny gold'], data)
    return(len(bags))


def part2(data):
    """How many are in the shiny gold bag ?"""
    total = what_is_in('shiny gold', data)
    return total-1


def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    rules = [rule_parser(rule) for rule in data]
    print('Part1: %d' % part1(rules))
    print('Part2: %d' % part2(rules))


if __name__ == "__main__":
    main()
