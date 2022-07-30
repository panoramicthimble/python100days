'''
TODO:
Chips?
Reshuffle dech...
  finding a random value between 0 and 0 breaks pretty spectacularly


Helpful Links
https://www.onlinegambling.com/blackjack/rules/
'''

# Cards exist in hands and also in the deck... they are not removed.
statistical_impossibility = False

# Asserts that player cards were two two's.
test_ace = True
test_split = False

# Modify end point if necessary      (add dealer hit/stand variable?) current logic was max - 4.
twentyone = 21


'''Program start'''
# General flow --> creates player and PC [hands] --> draw_card() x4 --> play_hand()

import random as rn
from art import logo
print(logo)

# Sets up deck
card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
if not statistical_impossibility:
  #card_values = card_values * 4
  print(card_values)


def draw_card():
  deck_size = len(card_values)-1
  next_card = card_values[rn.randint(0, deck_size)]
  if not statistical_impossibility:
    card_values.remove(next_card)
    ''''''#print(card_values)#log
  return next_card
  

def play_game(P1_hand, PC_hand):

  P1_hand = []
  PC_hand = []
  
  P1_hand.append(draw_card())
  PC_hand.append(draw_card())
  P1_hand.append(draw_card())
  PC_hand.append(draw_card())

  if test_ace:
    P1_hand = [11, 3]

  if test_split:
    P1_hand = [2, 2]
  
  player_total = sum(P1_hand)
  print(f"Your cards: {P1_hand}, current score: {player_total}\nComputer's first card: {PC_hand[0]}")

  hands = [P1_hand, PC_hand]
  
  if P1_hand[0] == P1_hand[1]:
    split = input(f"Two {P1_hand[0]}s, will you split them? Type 'y' for yes, 'n' for no: ").lower()
  else:
    split = 'n'
  # This loop auto completes if split was just set to 'n'
  accepted = False
  while not accepted:
    if split == 'y' or split == 'n':
      accepted = True
    else:
      split = input("That wasn't an accepted response, type 'y' or 'n': ")
  
  if split == 'y':
    card = P1_hand[0]
    P1_hand.remove(card)
    ''''''#print(f"after removal: {P1_hand}")
    hands = [P1_hand, PC_hand]
    play_hand(hands) #disable replay somehow
    first_card = hands[0][0]
    hands[0] = []
    hands[0].append(first_card)
    hands[0].append(draw_card())
    play_hand(hands)
    
  if split == 'n':
    ''''''#print(f"Init hand with {P1_hand}")
    play_hand(hands)


def play_hand(hands):
  P1_hand = hands[0]
  ''''''#print(f"player hand: {P1_hand}")
  PC_hand = hands[1]
  playing_split = False
  if len(P1_hand) == 1:
    playing_split = True
    P1_hand.append(draw_card())
  ''''''#print(f"Playing: {P1_hand}")#log
  total = sum(P1_hand)
  hands = [P1_hand, PC_hand]
  if total == 21:
    print("BlackJack! Congratulations! You win!")
    if not playing_split:
      play_again()
  else:
    hit_stand(hands, playing_split)
  

def hit_stand(hands, playing_split):
  ''''''#print(f"playing split: {playing_split}")
  P1_hand = hands[0]
  PC_hand = hands[1]
  print(f"Playing: {P1_hand}")
  # Gets hit or stand
  done = False
  while not done:
    hit = input("Would you like to hit (h) or stand (s): ")
    if hit != 'h' and hit != 's':
      hit = input("That wasn't an option, type 'h' for hit or 's' for stand: ")
      continue
    else:
      done = True
      
    # Draws another card (hits)
    if hit == 'h':
      next_card = draw_card()
  
      P1_hand.append(next_card)
      player_total = sum(P1_hand)
      a = "a"
      if next_card == 8:
        a = "an"
      print(f"You drew {a} {next_card}.")
      if player_total > twentyone:
        for card in P1_hand:
          if card == 11 and player_total > 21:
            P1_hand.remove(card)
            P1_hand.insert(0, 1)
            player_total = sum(P1_hand)
      print(f"Your score is: {player_total}")
      hands = [P1_hand, PC_hand]
      if player_total < twentyone:
        hit_stand(hands, playing_split)
      else:
        determine_winner(P1_hand, PC_hand, playing_split)


    # Finishes players round (stands)
    if hit == 's':
      print("Standing")
      determine_winner(P1_hand, PC_hand, playing_split)

      
# Takes finished player hand, and initialized computer hand.
def determine_winner(P1_hand, PC_hand, playing_split):
  player_total = sum(P1_hand)
  opponent_total = sum(PC_hand)
  if player_total > 21:
    print(f"Your hand: {player_total}   Bust! You lose.")
  else:
    while opponent_total < twentyone - 4:
      # TODO: hit with a 'soft' 17
      deck_size = len(card_values)-1
      next_card = card_values[rn.randint(0, deck_size)]
      if not statistical_impossibility:
        card_values.remove(next_card)
        print(card_values)#log
      PC_hand.append(next_card)
      opponent_total = sum(PC_hand)
      print(opponent_total)#log
    if opponent_total > twentyone:
      print(f"Dealer's score: {opponent_total}    Bust! You win.")
    else:
      result = "You lose"
      if player_total > opponent_total:
        result = "You win"
      elif player_total == opponent_total:
        result = "It's a push.."
      print(f"Your score was {player_total}, {P1_hand} against the dealer's {opponent_total}, {PC_hand}. {result}.")
  if not playing_split:
    play_again()


# Resets game state
def play_again():
  # if not statistical_impossibility:
  #   if len(card_values)<20:
  #     card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
      #card_values = card_values * 4
      #print(card_values)
  again = input("Would you like to play again?").lower()
  if again == 'y' or again == 'n':
    reset = True
  while not reset:
    print("That wasn't an option, sorry. Please pick 'n' or 'y'")
    play_again()
  if again == 'y':
    play_game(P1_hand, PC_hand)
  else:
    print("Alright, thanks for playing!")


### Begin ###
P1_hand = []
PC_hand = []

play_game(P1_hand, PC_hand)

'''
class Game:
  def __init__(self, round, cash):
    self.round = 0
    self.cash = 300

game = Game()

# def set_board(continuing):
#   if not continuing:
#     proceed = input("How about a game of BlackJack?")
#   else:
#     proceed = input("Would you like to play again?")

def set_board(game):
  game.round += 1
  if game.round <= 1:
    proceed = input("How about a game of BlackJack?")
  else:
    proceed = input("Would you like to play again?")
  
'''