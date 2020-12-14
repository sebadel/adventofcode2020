#!/usr/bin/env python


def part1(ts, schedule):
    buses = [int(bus) for bus in schedule.split(',') if bus != 'x']
    best_next_dep = ts
    best_bus = None
    for bus in buses:
        next_dep = ts + bus - (ts % bus) 
        if next_dep < ts + best_next_dep:
            best_next_dep = next_dep - ts
            best_bus = bus
    return best_bus * best_next_dep


def part2(schedule):
    schedule = schedule.replace('x', '0')
    buses = [int(bus) for bus in schedule.split(',')]
    ts, step = 0, buses[0]
    for i, bus in filter(lambda x: x[1], enumerate(buses[1:], start=1)):
        while (ts + i) % bus != 0:
            ts += step
            print(ts)
        print('step = step * b ==> %d = %d * %d' % (step * bus, step, bus))
        step *= bus
    return ts


def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    ts = int(data[0])
    schedule = data[1]
    print(part1(ts, schedule))
    print('Part 2: %s' % part2(schedule))
    print('Part 2: %s' % part2('3,5,7'))


if __name__ == "__main__":
    main()
