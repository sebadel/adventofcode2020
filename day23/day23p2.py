#!/usr/bin/env python


class Game():
    def __init__(self, data, n=1000000):
        data = [int(x) for x in data]
        self.data = {}
        for i, x in enumerate(data, start=1):
            if i < len(data):
                self.data[x] = data[i]
            else:
                self.data[x] = data[0]
        data = [int(x) for x in list(data)]
        self.current = data[0]
        if len(data) < n:  # Increase the number of cups
            last = data[-1]
            max_x = max(data)
            self.data[last] = max_x + 1  # Open the circle
            while len(self.data) < n:
                max_x += 1
                self.data[max_x] = max_x + 1  # Add cups
            self.data[max_x] = self.current  # Close the circle.
        self.min = min(self.data.keys())
        self.max = max(self.data.keys())

    def move(self):
        three_cups = [
            self.next(self.current),
            self.next(self.next(self.current)),
            self.next(self.next(self.next(self.current)))
        ]
        d = self.destination(self.current, three_cups)
        self.data[self.current] = self.data[three_cups[2]]
        self.data[three_cups[2]] = self.next(d)
        self.data[d] = three_cups[0]
        self.current = self.next(self.current)

    def print_data(self):
        safeguard = 0
        x = self.current
        while True:
            safeguard += 1
            if x == self.current:
                print('(%d)' % x, end=' ')
            else:
                print('%d' % x, end=' ')
            x = self.next(x)
            if x == self.current:
                break
        print()

    def destination(self, current, exceptions):
        if current == self.min:
            x = self.max
        else:
            x = current - 1
        if x in exceptions:
            return self.destination(x, exceptions)
        return x

    def next(self, cup):
        return self.data[cup]


def part2(data, n=1000000, rounds=10000000):
    game = Game(data, n)
    round = 1
    while round <= rounds:
        round += 1
        # game.print_data()
        game.move()
    print('%d * %d = %d' % (
        game.next(1),
        game.next(game.next(1)),
        game.next(game.next(1)) * game.next(1)
    ))
    return game.next(game.next(1)) * game.next(1)


def main():
    data = '135468729'
    print('Part 2: %s' % part2(data))


if __name__ == "__main__":
    main()
