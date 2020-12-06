#!/usr/bin/env python


def part1(data):
    total = 0
    questions = set()
    for line in data:
        if not line:
            total += len(questions)
            questions = set()
        else:
            questions.update([c for c in line])
    return total


def part2(data):
    total = 0
    answers = set([c for c in 'abcdefghijklmnopqrstuvwxyz'])
    for line in data:
        if not line:
            total += len(answers)
            answers = set([c for c in 'abcdefghijklmnopqrstuvwxyz'])
        else:
            answers = answers.intersection([c for c in line])
    return total


def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    print('Part 1: %s' % part1(data))
    print('Part 2: %s' % part2(data))


if __name__ == "__main__":
    main()
