#!/usr/bin/env python


import queue


def part1(data):
    player1 = queue.Queue()
    player2 = queue.Queue()
    for card in data[data.index('Player 1:') + 1:data.index('')]:
        player1.put(int(card))
    for card in data[data.index('Player 2:')+1:]:
        player2.put(int(card))
    while not player1.empty() and not player2.empty():
        card1 = player1.get()
        card2 = player2.get()
        if card1 > card2:
            player1.put(card1)
            player1.put(card2)
        else:
            player2.put(card2)
            player2.put(card1)
    winner = player1 if player1.qsize() > player2.qsize() else player2
    total = 0
    while not winner.empty():
        total += winner.qsize() * winner.get()
    return total


def part2(data):
    pass


def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    print('Part 1: %s' % part1(data))
    print('Part 2: %s' % part2(data))


if __name__ == "__main__":
    main()
