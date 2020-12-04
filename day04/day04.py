#!/usr/bin/env python

import re

RE_SIZE = re.compile(r'(\d+)((in|cm))')


def part1(data):
    """
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)
    """     
    passport = {}
    count = 0
    fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']) #, 'cid']
    for line in data:
        if not line:
            if fields.issubset(set(passport.keys())): count += 1                 
            passport = {}
        else:
            for pair in line.split(' '):
                k, v = pair.split(':')
                passport[k] = v
    return count


def part2(data):
    """
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    """
    passport = {}
    count = 0
    fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']) #, 'cid']
    for line in data:
        if not line:  # Check passport validity
            if (
                fields.issubset(set(passport.keys())) and                 
                int(passport['byr']) in range(1920, 2003) and
                int(passport['iyr']) in range(2010, 2021) and
                int(passport['eyr']) in range(2020, 2031) and
                re.match(r'^\d{9}$', passport['pid']) and
                check_size(passport['hgt']) and
                check_ecl(passport['ecl']) and
                check_hcl(passport['hcl'])
            ):
                count += 1
            passport = {}
        else:  # Add fields to passport
            for pair in line.split(' '):
                k, v = pair.split(':')
                passport[k] = v
    return count


def check_size(size):
    """
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.

    From Python 3.8, it is possible to use the walrus operator.
    e.g.: m := RE_SIZE.match(size) and (m.groups() ...)
    """
    m = RE_SIZE.match(size)
    return (
        m and (
            (m.groups()[1] == 'cm' and int(m.groups()[0]) in range(150, 294)) or
            (m.groups()[1] == 'in' and int(m.groups()[0]) in range(59, 77))
        )
    )
 

def check_hcl(s):
    """
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    """
    return re.match(r'^\#[0-9a-f]{6}$', s)


def check_ecl(s):
    """
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    """
    return s in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def main():
    data = [l.strip() for l in open('input.txt', 'r').readlines()]
    print('Part 1: %d' % part1(data))
    print('Part 2: %d' % part2(data))


if __name__ == "__main__":
    main()
