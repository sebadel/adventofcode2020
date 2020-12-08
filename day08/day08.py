#!/usr/bin/env python


def part1(data):
    c = 0
    i = 0
    instructions = []
    while True:
        line = data[i]
        if i in instructions:
            return c
        instructions.append(i)
        op, x = line.split(' ')
        if op == 'acc':
            c += int(x)
            i += 1

        elif op == 'jmp':
            i += int(x)
        else:
            i += 1
    return c


def sanitize_data(data):
    """Getting rid of empty lines at the end of the input file."""
    while not data[-1]:
        del data[-1]


def execute(data):
    c = 0
    i = 0
    instructions = []
    while True:
        op, x = data[i].split(' ')
        if i == len(data)-1:  # Reached the end of the instruction set.
            return c
        if i in instructions:  # Loop.
            return False
        instructions.append(i)
        if op == 'jmp':
            i += int(x)
        else:
            i += 1
        if op == 'acc':
            c += int(x)


def swap_operator(data, i):
    operators = ['jmp', 'nop']
    op, x = data[i].split(' ')
    if op in operators:
        op = 'jmp' if op == 'nop' else 'nop'
        data[i] = '%s %s' % (op, x)


def part2(data):
    i = 0
    while i < len(data):
        print('Changing %i - %s ...' % (i, data[i]))
        swap_operator(data, i)
        result = execute(data)
        if result:
            return result
        swap_operator(data, i)
        i += 1


def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    sanitize_data(data)
    print('Part 1: %s' % part1(data))
    print('Part 2: %s' % part2(data))


if __name__ == "__main__":
    main()
