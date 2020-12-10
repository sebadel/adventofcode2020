#!/usr/bin/env python


from functools import lru_cache


def part2(data):
    # Let's try without the options...  not working - data is unhashable
    # return try_adapter(data, 0)
    return try_adapter_lru_wrapper(data, 0)


# @lru_cache(maxsize=None)
# def try_adapter(data, cursor):
#     if cursor == len(data)-1:
#         return 1
#     i = 1
#     cnt = 0
#     while cursor+i < len(data):
#         if data[cursor+i] - data[cursor] < 4:
#             cnt += try_adapter(data, cursor+i)
#         i += 1
#     return cnt


def try_adapter_lru_wrapper(data, cursor):
    @lru_cache(maxsize=None)
    def try_adapter(cursor):
        if cursor == len(data)-1:
            return 1
        i = 1
        cnt = 0
        while cursor+i < len(data):
            if data[cursor+i] - data[cursor] < 4:
                cnt += try_adapter(cursor+i)
            i += 1
        return cnt
    return try_adapter(cursor)


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
    print('Part 2 ... faster: %s' % part2(data))


if __name__ == "__main__":
    main()
