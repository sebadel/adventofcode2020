#!/usr/bin/env python

"""
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

4               1               5
a               2 3 | 3 2       b
a               44|55 45|54 | 45|54 44|55       b
a               aa|bb ab|ba | ab|ba aa|bb       b
"""
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


def develop_rule(rule, rules):
    if '|' in rule:
        return '(%s)' % '|'.join([
            develop_rule(rule[0:rule.index('|')], rules),
            develop_rule(rule[rule.index('|') + 1:], rules)
        ])
    rule = re.sub(r'\d+', lambda x: develop_rule(rules[int(x.group())], rules), rule)
    return rule.replace('"', '').replace(' ', '')

def _join(s):
    if isinstance(s, list):
        return '[%s]' % _join(''.join([_join(x) for x in s]))
    return s


def part1(data):
    count = 0
    rules, messages = parse_input(data)
    valid = develop_rule(rules[0], rules)
    valid = '^%s$' % _join(valid)
    matcher = re.compile(valid)
    for message in messages:
        print(message, end=' ')
        if matcher.match(message):
            print('OK')
            count += 1
        else:
            print('')
#    return len(set(valid).intersection(set(messages)))
    return count


def develop_rule2(rule, rules):
    if '|' in rule:
        return '(%s)' % '|'.join([
            develop_rule2(rule[0:rule.index('|')], rules),
            develop_rule2(rule[rule.index('|') + 1:], rules)
        ])
    rule = re.sub(r'\d+', lambda x: develop_rule2(rules[int(x.group())], rules), rule)
    return rule.replace('"', '').replace(' ', '')

def part2(data):
    count = 0
    rules, messages = parse_input(data)
    rules[8] = '42 | 42 8'
    rules[11] = '42 31 | 42 11 31'
    rules[8] = '42+'
    rules[11] = '42 (42 31)* 31' # 398 => wrong 42 42 31 42 31 31
    rules[11] = '42+ 31+' # 424  => wrong 42 42 31
    valid = develop_rule(rules[0], rules)
    print(develop_rule(rules[42], rules))
    print(develop_rule(rules[31], rules))
    print(valid)
    valid = '^%s$' % _join(valid)
    matcher = re.compile(valid)
    for message in messages:
        print(message, end=' ')
        if matcher.match(message):
            print('OK')
#            print('%d - %d' % (
#                len(re.findall(develop_rule(rules[42], rules), message)),
#                len(re.findall(develop_rule(rules[31], rules), message)),
#            ))
#            if (len(re.findall(develop_rule(rules[42], rules), message)) ==
#                len(re.findall(develop_rule(rules[31], rules), message))):
            count += 1
        else:
            print('')
    return count
# 399 < x # 424
# 410 411 not good either

def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    print('Part 1: %s' % part1(data))
    print('Part 2: %s' % part2(data))


if __name__ == "__main__":
    main()
