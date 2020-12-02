#!/usr/bin/env python

import re


class PasswordLine():
    def __init__(self, line):
        self.line = line.strip()
        self.min = 0
        self.max = 0
        self.char = ''
        self.password = ''
    
    def parse(self):
        match = re.match(r"(\d+)-(\d+)\s(\w)\:\s(.*)", self.line)
        if match:
            self.min, self.max, self.char, self.password = match.groups()
        self.min = int(self.min)
        self.max = int(self.max)
    
    def valid(self):
        if not self.password:
            self.parse()
        return self.min <= self.password.count(self.char)  and self.password.count(self.char) <= self.max

    def valid_part2(self):
        if not self.password:
            self.parse()
        return (
            (self.password[self.min-1] == self.char) != 
            (self.password[self.max-1] == self.char)
        )


def part1(data):
    print(len([l for l in data if l.valid()]))


def part2(data):
    print(len([l for l in data if l.valid_part2()]))


def main():
    data = open('input.txt', 'r').readlines()
    data = [PasswordLine(line) for line in data]
    part1(data)
    part2(data)


if __name__ == "__main__":
    main()
