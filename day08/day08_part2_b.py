#!/usr/bin/env python

import copy


def sanitize_data(data):
    """Getting rid of empty lines at the end of the input file."""
    while not data[-1]:
        del data[-1]


def swap_operator(data, i):
    operators = ['jmp', 'nop']
    op, x = data[i].split(' ')
    if op in operators:
        op = 'jmp' if op == 'nop' else 'nop'
        data[i] = '%s %s' % (op, x)


def is_loop(data, total=0, cursor=0):
    if not data[cursor]: # Loop detected
        return -1
    op, x = data[cursor].split(' ')
    data[cursor] = False  # Leaving a footprint where we have been
    cursor +=  int(x) if op == 'jmp' else 1
    total += int(x) if op == 'acc' else 0 
    if cursor == len(data): # End of instruction set reached
        return total
    return is_loop(data, total, cursor)


def part2(data):
    for i, line in enumerate(data):
        instructions = copy.deepcopy(data)
        swap_operator(instructions, i)
        result = is_loop(instructions)
        if result > 0:
            return result
    return 'Could not find a non-loop path.'


    
def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    sanitize_data(data)
    print('Part 2: %s' % part2(data))


if __name__ == "__main__":
    main()
