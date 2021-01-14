#!/usr/bin/env python


def move(data, current):
    current_position = data.index(current)
    three_cups = []
    next_position = (current_position + 1) % len(data)
    three_cups.append(data.pop(next_position))
    next_position = next_position % len(data)
    three_cups.append(data.pop(next_position))
    next_position = next_position % len(data)
    three_cups.append(data.pop(next_position))
    try:
        destination = max([x for x in data if x < current])
    except ValueError:
        destination = max(data)
    three_cups.reverse()
    for tc in three_cups:
        data.insert(data.index(destination)+1, tc)
    current = data[(data.index(current) + 1) % len(data)]
    return data, current


def part1(data):
    data = [int(x) for x in list(data)]
    current = data[0]
    round = 1
    while round <= 100:
        round += 1
        data, current = move(data, current)
    output = []
    while len(data) > 1:
        output.append(str(
            data.pop((data.index(1)+1) % len(data))
        ))
    return ''.join(output)


def main():
    data = '135468729'
    print('Part 1: %s' % part1(data))


if __name__ == "__main__":
    main()
