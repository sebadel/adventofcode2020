#!/usr/bin/env python

import re


def parse_input(data):
    """Returns rules, messages."""
    rules = {}
    messages = []
    for line in data:
        if ': ' in line:
            rule_id, rule = line.split(': ')
            rules[int(rule_id)] = rule  # .split(' ')
        else:
            messages.append(line)
    return rules, messages


def develop_rule(rules, rule_id=0):
    rule = rules[rule_id]
    if rule in ['a', 'b']:
        return rule
    rule = re.sub(r'\d+', lambda x: develop_rule(rules, int(x.group())), rule)
    if '|' in rule:
        rule = '(%s)' % rule
    return rule.replace('"', '').replace(' ', '')


def develop_rule2(rules, rule_id=0):
    rules[8] = '42+'
    rule = rules[rule_id]
    if rule in ['a', 'b']:
        return rule
    if rule_id == 11:
        max_occurrences = 12  # arbitrary value
        r11 = []
        for n in range(0, max_occurrences):
            r11.append('(%s%s)' % (
                '42 ' * n,
                '31 ' * n))
        rule = '42 (%s)? 31' % '|'.join(r11)
    rule = re.sub(r'\d+', lambda x: develop_rule2(rules, int(x.group())), rule)
    if '|' in rule:
        rule = '(%s)' % rule
    return rule.replace('"', '').replace(' ', '')


def _join(s):
    if isinstance(s, list):
        return '[%s]' % _join(''.join([_join(x) for x in s]))
    return s


def part1(data):
    count = 0
    rules, messages = parse_input(data)
    valid = develop_rule(rules)
    valid = '^%s$' % _join(valid)
    matcher = re.compile(valid)
    for message in messages:
        if matcher.match(message):
            count += 1
    return count


def part2(data):
    count = 0
    rules, messages = parse_input(data)
    valid = develop_rule2(rules)
    valid = '^%s$' % _join(valid)
    matcher = re.compile(valid)
    for message in messages:
        if matcher.match(message):
            count += 1
    return count


def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    print('Part 1: %s' % part1(data))
    print('Part 2: %s' % part2(data))


if __name__ == "__main__":
    main()
