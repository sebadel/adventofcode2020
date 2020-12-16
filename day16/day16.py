#!/usr/bin/env python


def parse_input(data):
    """Returns rules, my_ticket, nearby_tickets."""
    rules = []
    tickets = []
    parsing_rules = True
    for line in data:
        if len(line) == 0:
            next
        elif line == 'your ticket:' or line == 'nearby tickets:':
            parsing_rules = False  # Start parsing tickets.
        elif parsing_rules:
            rules.append(Rule(line))
        else:
            tickets.append(Ticket(line))
    my_ticket = tickets.pop(0)
    return rules, my_ticket, tickets


class Rule(object):
    def __init__(self, rule_str):
        self.name, props = rule_str.split(': ')
        range1, range2 = props.split(' or ')
        self.min1, self.max1 = [int(x) for x in range1.split('-')]
        self.min2, self.max2 = [int(x) for x in range2.split('-')]
        self.possible_fields = []

    def match(self, n):
        return (
            n in range(self.min1, self.max1 + 1) or
            n in range(self.min2, self.max2 + 1))

    def set_possible_fields(self, tickets):
        i = 0
        while i < len(tickets[0].fields):
            possible = True
            for ticket in tickets:
                if not self.match(ticket.fields[i]):
                    possible = False
            if possible:
                if i not in self.possible_fields:
                    self.possible_fields.append(i)
            i += 1

    def certain(self):
        return len(self.possible_fields) == 1


class Ticket(object):
    def __init__(self, ticket_str):
        self.fields = [int(x) for x in ticket_str.split(',')]

    def valid(self, rules):
        """All fields of this ticket match at least one rule."""
        return self.first_invalid_field(rules) == -1

    def first_invalid_field(self, rules):
        """First field that does not match any rule."""
        for field in self.fields:
            this_field_matches_at_least_one_rule = False
            for rule in rules:
                if rule.match(field):
                    this_field_matches_at_least_one_rule = True
            if not this_field_matches_at_least_one_rule:
                return field
        return -1


def rule_only_possible_field(rules):
    certainty = {}
    done = False
    while not done:
        done = True
        certain_rules = [r for r in rules if r.certain()]
        if certain_rules:
            done = False
            rule = certain_rules[0]
            rules.remove(rule)
            field = rule.possible_fields[0]
            certainty[rule.name] = field
            for rule in rules:
                if field in rule.possible_fields:
                    rule.possible_fields.remove(field)
    return certainty


def part1(tickets, rules):
    error_rate = 0
    for ticket in tickets:
        if not ticket.valid(rules) and ticket.first_invalid_field(rules) != -1:
            error_rate += ticket.first_invalid_field(rules)
    return error_rate


def part2(my_ticket, tickets, rules):
    valid_tickets = [t for t in tickets if t.valid(rules)]
    for rule in rules:
        rule.set_possible_fields(valid_tickets)
    only_possible_fields = rule_only_possible_field(rules)
    product = 1
    for name in sorted(only_possible_fields):
        if 'departure' in name:
            product *= my_ticket.fields[only_possible_fields[name]]
    return product


def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    rules, my_ticket, nearby_tickets = parse_input(data)
    print('Part 1: %s' % part1(nearby_tickets, rules))
    print('Part 2: %s' % part2(my_ticket, nearby_tickets, rules))


if __name__ == "__main__":
    main()
