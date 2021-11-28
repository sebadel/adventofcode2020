#!/usr/bin/env python

import logging
import re


RE_INNER_PARENTHESIS = re.compile(r'\(([^()]*)\)')
RE_OPERATION = re.compile(r'^(\d+[+:*/]\d+)')

def _print(c):
    print(' -- %s -- ' % c)
    return eval(c)

def test(expr):
    print('test => %s' % expr)
    if isinstance(expr, int):
        expr = str(expr)
    expr = expr.replace(' ', '')
    if RE_INNER_PARENTHESIS.match(expr):
        return test(
            RE_INNER_PARENTHESIS.sub(
                lambda a: a.groups()[0], expr))
    if RE_OPERATION.match(expr):
        return test(
            RE_OPERATION.sub(
                lambda a: str(eval(a.groups()[0])), expr, 1))
    return eval(expr)


def evaluate(expr):
    m = RE_INNER_PARENTHESIS.match(expr)
    if m:
        return evaluate(
            ''.join([
                m.groups()[0],
                str(evaluate(m.groups()[1])),
                m.groups()[2]
            ]))
    m = RE_OPERATION.match(expr)
    if m:
        return evaluate(''.join( [str(eval(m.groups()[0])), m.groups()[1]] ))
    else:
        return eval(expr)

RE_SUM = re.compile(r'(.*?)(\d+[+-]\d+)(.*)')
def evaluate_p2(expr):
#    print(expr)
    m = RE_INNER_PARENTHESIS.match(expr)
    if m:
        return evaluate_p2(
            ''.join([
                m.groups()[0],
                str(evaluate_p2(m.groups()[1])),
                m.groups()[2]
            ]))
    m = RE_SUM.match(expr)
    if m:
        return evaluate_p2(
            ''.join([
                m.groups()[0],
                str(eval(m.groups()[1])),
                m.groups()[2]
            ]))
    else:
        return eval(expr)


def part1(data):
    sum = 0
    for l in data:
        sum += test(l)
    return sum


def part2(data):
    sum = 0
    for l in data:
        l = l.replace(' ', '')
        sum += evaluate_p2(l)
    return sum


def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    #data = ['1 + (2 * 3) + (4 * (5 + 6))']
#    data = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
    print('Part 1: %s' % part1(data))
#    print('Part 2: %s' % part2(data))


if __name__ == "__main__":
    main()
