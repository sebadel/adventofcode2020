#!/usr/bin/env python


def find_loop_size(n, encryption_key):
    x = 1
    loop_size = 0
    print('finding %d ...' % encryption_key)
    while x != encryption_key:
        x = x * n
        x = x % 20201227
        loop_size += 1
    return loop_size

def encode(n, loop_size):
    x = 1
    loop = 0
    while loop < loop_size:
        x = x * n
        x = x % 20201227
        loop += 1
    return x

def part1(data):
    card_key, door_key = data
    card_loop_size = find_loop_size(7, int(card_key))
    print(card_loop_size)
    door_loop_size = find_loop_size(7, int(door_key))
    print(door_loop_size)
    print('card encryption key:')
    print(encode(int(door_key), card_loop_size))
    print('door encryption key:')
    print(encode(int(card_key), door_loop_size))


def part2(data):
    pass


def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    print('Part 1: %s' % part1(data))


if __name__ == "__main__":
    main()
