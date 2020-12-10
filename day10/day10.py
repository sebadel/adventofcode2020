#!/usr/bin/env python


def part1(data):
    steps = 0
    diffs = {1: [], 2: [], 3: []}
    jolts = 0
    i = 0
    data = sorted(data)
    while(i < len(data)-1):
        jolts += data[i]
        steps += 1
        diff = data[i+1] - data[i]
        diffs[diff].append(diff)
        if diff > 3:
            break
        i += 1
    return len(diffs[1]) * len(diffs[3])


def part2(data):
    return walk(data, 0)


def walk(data, cursor):
    # This works ... if you live long enough to see it ...
    if cursor == len(data)-1:
        return 1
    i = 1
    cnt = 0
    while cursor+i < len(data):
        if data[cursor+i] - data[cursor] < 4:
            cnt += walk(data, cursor+i)
        i += 1
    return cnt


def part2_faster(data):
    # Let's first build a list of the options to plug an adapter to another.
    # e.g.: {0: [1, 2, 3], 1: [2, 3, 4], 2: [3, 4], ...}
    options = {x: [x+i for i in range(1, 4) if x+i in data] for x in data}
    return try_options(0, options)


def try_options(i, options, tried={}):
    """
    Args:
        i: the adapter we want to try.
        options: the list of adapters and its options.
        tried: list of adapters we already tried.
    Returns:
        number of options it leads to.
    """
    if options[i] == []:
        return 1
    cnt = 0
    for o in options[i]:
        # we have not tried this adapter yet.
        if o not in tried:
            r = try_options(o, options, tried)
            # now that we have tried it, let's record how many options it
            # leads to.
            tried[o] = r
        cnt += tried[o]
    return cnt


def main():
    data = [int(line.strip()) for line in open('input.txt', 'r').readlines()]
    data.append(0)
    data.append(max(data)+3)
    data = sorted(data)
    print('Part 1: %d' % part1(data))
    # print('Part 2 ... super slow: %s' % part2(data))
    print('Part 2 ... faster: %s' % part2_faster(data))


if __name__ == "__main__":
    main()
