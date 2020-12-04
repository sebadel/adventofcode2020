#!/usr/bin/env python

import re

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

def part1(data):
    passport = {}
    count = 0
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] #, 'cid']
    for line in data:
        if not line:
            print(passport)
            valid = True
            for field in fields:
                if field not in passport:
                    valid = False
            if valid:
                count += 1
            passport = {}
        else:
            pairs = line.split(' ')
            for pair in pairs:
                pair = pair.split(':')
                passport[pair[0]] = pair[1]
    return count

"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""

def check_size(s):
    """
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    """
    counters['check_size'] += 1
    m = re.match(r'(\d+)cm', s)
    if m:
        return int(m.groups()[0]) in range(150,194)
    m = re.match(r'(\d+)in', s)
    if m:
        return int(m.groups()[0]) in range(59,77)
    return False

def check_hcl(s):
    """
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    """
    if re.match('^\#[0-9a-f]{6}$', s):
        return True
    print(s)
    return False

def check_ecl(s):
    """
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    """
    return s in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def part2(data):
    passport = {}
    count = 0
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] #, 'cid']
    for line in data:
        if not line:  # Check passport validity
            valid = True
            for field in fields:
                if field not in passport:
                    valid = False
            if valid:
                if (
                    int(passport['byr']) in range(1920,2003) and
                    int(passport['iyr']) in range(2010,2021) and
                    int(passport['eyr']) in range(2020,2031) and
                    check_size(passport['hgt']) and
                    check_ecl(passport['ecl']) and
                    check_hcl(passport['hcl']) and
                    re.match('^\d{9}$', passport['pid'])
                ):
                    count += 1
            passport = {}
        else:  # Add fields to passport
            pairs = line.split(' ')
            for pair in pairs:
                pair = pair.split(':')
                passport[pair[0]] = pair[1]
    return count

def main():
    data = [l.strip() for l in open('input.txt', 'r').readlines()]
    print('Part 1: %d' % part1(data))
    print('Part 2: %d' % part2(data))
    print(counters)

if __name__ == "__main__":
    main()
