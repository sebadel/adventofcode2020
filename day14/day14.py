#!/usr/bin/env python

import re


def part1(data):
    memory = {}
    for line in data:
        op, value = line.split(' = ')
        if op == 'mask': 
            mask = value
        else:
            address = int(re.search(r'mem\[(\d+)\]', op).groups()[0])
            value = format(int(value), '036b')
            memory[address] = apply_mask(value, mask)
    return reduce(lambda acc, x: acc + x, memory.values())


def apply_mask(value, mask):
    """Applies a mask to a binary string.
    Args:
        value: str
        mask: str
    Returns:
        int, based on binary representation of the value with the mask applied.
    """
    def _op(a, b):
        return a if b == 'X' else b

    return int(''.join([_op(a, b) for a, b in zip(value, mask)]), 2)


def part2(data):
    memory = {}
    for line in data:
        op, value = line.split(' = ')
        if op == 'mask': 
            mask = list(value)
        else:
            address = int(re.search(r'mem\[(\d+)\]', op).groups()[0])
            address = format(address, '036b')
            address = apply_address_mask(address, mask)
            for i, a in enumerate(expand_addresses(address)):
                memory[int(a, 2)] = int(value)
    return reduce(lambda acc, x: acc + x, memory.values())


def apply_address_mask(value, mask):
    converted = [a if b == '0' else b for a, b in zip(value, mask)]
    return ''.join(converted)


def expand_addresses(value):
    if 'X' not in value:
        return [value]
    else:
        values = []
        values.extend(expand_addresses(value.replace('X', '0', 1)))
        values.extend(expand_addresses(value.replace('X', '1', 1)))
        return values


def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    print('Part 1: %s' % part1(data))
    print('Part 2: %s' % part2(data))


if __name__ == "__main__":
    main()
