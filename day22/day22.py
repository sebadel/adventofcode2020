#!/usr/bin/env python

import copy
import itertools


def _deal(data):
  """Deals the cards, returns 2 queues for P1 and P2."""
  player1 = []
  player2 = []
  for card in data[data.index('Player 1:') + 1:data.index('')]:
      player1.append(card)
  for card in data[data.index('Player 2:') + 1:]:
      player2.append(card)
  return player1, player2


def part1(data):
    player1, player2 = _deal(data)
    while (len(player1) and len(player2)):
      card1 = player1.pop(0)
      card2 = player2.pop(0)
      if int(card1) > int(card2):
          player1.append(card1)
          player1.append(card2)
      else:
          player2.append(card2)
          player2.append(card1)
    winner = player1 if len(player1) > len(player2) else player2
    total = 0
    return deck_value(winner)


def deck_value(deck):
  value = 0
  while len(deck) > 0:
    value += len(deck) * int(deck[0])
    deck.pop(0)
  return value


def save_deck(deck_history, player1, player2):
  """Keeps track of encountered decks for loop detection."""
  p1 = ','.join(player1)
  p2 = ','.join(player2)
  if p1 not in deck_history:
    deck_history[p1] = [p2]
  else:
    deck_history[p1].append(p2)


def idem(deck_history, player1, player2):
  """Returns True if this exact deck combination has already been played."""
  hp1 = ','.join(player1)
  if hp1 in deck_history:
    if ','.join(player2) in deck_history[hp1]:
      return True
  return False

def show_game(p1, p2):
  print('%s / %s' % (','.join([x for x in p1]), ','.join([x for x in p2])))


def copy_and_slice_queue(q, n):
  """Slices a copy of a FIFO queue to n first elements."""
  return copy.copy(q)[0:n]


def game(deck_history, player1, player2, game_cnt=0):
  """Recursive game called in part2."""
  winner = False
  deck_history = {}
  print('[Game %d] - P1:%d cards --- P2:%d cards' % (
      game_cnt,
      len(player1), len(player2)))
  while not winner:

    # Check if we are in a loop
    if idem(deck_history, player1, player2):
      print('Loop')
      return player1, player2, player1
    save_deck(deck_history, player1, player2)

    # Check if both players still have cards
    if len(player1) == 0:
      print('Player1 empty')
      return player1, player2, player2
    if len(player2) == 0:
      print('Player2 empty')
      return player1, player2, player1

    # Play round
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    if len(player1) >= int(card1) and len(player2) >= int(card2):
      p1, p2, x = game(
          deck_history, copy_and_slice_queue(player1, int(card1)),
          copy_and_slice_queue(player2, int(card2)), game_cnt = game_cnt+1)
      if p1 == x:
        player1.append(card1)
        player1.append(card2)
      else:
        player2.append(card2)
        player2.append(card1)
    else:
      if int(card1) > int(card2):
        player1.append(card1)
        player1.append(card2)
      else:
        player2.append(card2)
        player2.append(card1)
  return player1, player2, winner


def part2(data):
  deck_history = {}
  player1, player2 = _deal(data)
  player1, player2, winner = game(deck_history, player1, player2)
  return(deck_value(winner))


def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    print('Part 1: %s' % part1(data))
    print('Part 2: %s' % part2(data))


if __name__ == "__main__":
    main()
