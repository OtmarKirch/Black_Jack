import random
from art import logo

def deal_hand():
  '''Deals one hand of two cards, represented as a list with two numbers'''
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  hand = []
  for number in range(0, 2):
    hand.append(cards[random.randint(0, len(cards) - 1)])
  return hand

def add_card(hand):
  '''Adds one card to the hand, adding it to the list.'''
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  hand.append(cards[random.randint(0, len(cards) - 1)])
  return hand

def deal_starting_hands():
  '''Deals a hand to the player and computer returned as a dictionary.'''
  player_cards = deal_hand()
  computer_cards = deal_hand()
  hands = {"player": player_cards, "computer": computer_cards}
  return hands

def check_card_sum(hand):
  '''Returns the sum of the string "hand". Takes into account, that a
  11 can be counted as 1 or 11. The function maximizes the possibility
  to get close to 21 without going over 21.'''
  hand.sort()
  occ_11 = hand.count(11)
  count_hand = 0
  for card in hand:
    if card != 11:
      count_hand += card
    else:
      count_hand += 1

  for occ in range(0, occ_11+1):
    if count_hand + 10 <= 21:
      count_hand += 10

  return count_hand

def play():
  '''Handles the game.'''
  quit_game = False
  while not quit_game:
    print(logo)
    print("Welcome to a round of Black Jack!")
    end = False
    hands = deal_starting_hands()

    while not end:
      if check_card_sum(hands["player"]) < 22:
        print(f"Your cards: {hands['player']}")
        print(f"Computer cards: {[hands['computer'][0],'X']}")
        y_n = input("Do you want another card? y or n?")
        while y_n != "n" and y_n != "y":
          y_n = input("Please type y or n!")
        if y_n == "y":
          hands['player'] = add_card(hands['player'])
          print(hands['player'])
        else:
          end = True

          while check_card_sum(hands["player"]) >= check_card_sum(hands["computer"]):
            hands['computer'] = add_card(hands['computer'])

          player_l = check_card_sum(hands["player"]) < check_card_sum(hands["computer"])
          computer_21 = check_card_sum(hands["computer"]) <= 21
          if player_l and computer_21:
            print("You lost:")
          else:
            print("You win!")
          print(f"Your hand {hands['player']}: {check_card_sum(hands['player'])},")
          print(f"Computer hand {hands['player']}: {check_card_sum(hands['computer'])}")
      else:
        print(f"Your score is {check_card_sum(hands['player'])}. You lost!")
        end = True

    play_again = input("Play again? y or n")
    while play_again != "n" and play_again != "y":
      play_again = input("Pleas type y or n")
      if play_again == "n":
        quit_game = True

play()
