#!/usr/bin/env python


import re


class Food():
    def __init__(self):
        self.ingredients = set()
        self.allergens = set()


def parse_line(line):
    f = Food()
    ingredients, allergens = re.match(
        r'(.*?)\s\(contains\s(.*)\)', line).groups()
    f.ingredients = set(ingredients.split(' '))
    f.allergens = set(allergens.split((', ')))
    return f


def part1(data):
    foods = [parse_line(line) for line in data]
    all_ingredients = set.union(*[f.ingredients for f in foods])
    all_allergens = set.union(*[f.allergens for f in foods])
    allergens_to_ingredients = {a: set.intersection(*[
        f.ingredients for f in foods if a in f.allergens
    ]) for a in all_allergens}
    with_allergens = set.union(*[
        allergens_to_ingredients[a] for a in all_allergens])
    without_allergens = all_ingredients.difference(with_allergens)
    sum_ing = sum([
        len(f.ingredients.intersection(without_allergens)) for f in foods])
    return sum_ing


def part2(data):
    foods = [parse_line(line) for line in data]
    all_allergens = set.union(*[f.allergens for f in foods])
    allergens_to_ingredients = {a: set.intersection(*[
        f.ingredients for f in foods if a in f.allergens
    ]) for a in all_allergens}
    done = False
    a_i = {}
    while not done:
        done = True
        for k, v in allergens_to_ingredients.items():
            if len(v) == 1:  # Identify pairs
                i = v.pop()
                a_i[k] = i
                done = False
                # Remove this ingredient from the other allergen sources.
                for k, v in allergens_to_ingredients.items():
                    if i in v:
                        v.remove(i)
    return ','.join([a_i[k] for k in sorted(a_i)])


def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    print('Part 1: %s' % part1(data))
    print('Part 2: %s' % part2(data))


if __name__ == "__main__":
    main()
