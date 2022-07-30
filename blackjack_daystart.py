import random as rn
from art import logo
print(logo)
'''
TODO:
Assign varying values to the Ace, depending on hand
Chips?
play again implementation

Helpful Links
https://www.onlinegambling.com/blackjack/rules/
'''


statistical_impossibility = True
twentyone = 21

card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#card_values = card_values * 4
#print(card_values)

def play_again():
  again = input("Would you like to play again?").lower()
  while again != 'n' and input != 'y':
    again = input("That wasn't an option, type 'n' to quit or 'y' to play again.")
  if again == 'n':
    print("Alright, thanks for playing!")
  else:
    print("Arrgh. Please restart.")

def draw_card():
  deck_size = len(card_values)-1
  next_card = card_values[rn.randint(0, deck_size)]
      # if not statistical_impossibility:
      #   card_values.remove(next_card)
  return next_card


def hit_stand():
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
      print(f"Your score is: {player_total}")
      ###
      # if player_total >= twentyone:
      #   determine_winner(P1_hand, PC_hand)
      # else:
      #   hit_stand()
      ###
      # Devil's advocate goes:
      if player_total < twentyone:
        hit_stand()
      else:
        determine_winner(P1_hand, PC_hand)
        return PC_hand
        # Man, I looooooooove Python.
      

        
    # Finishes players round (stands)
    if hit == 's':
      print("Standing")
      determine_winner(P1_hand, PC_hand)

def determine_winner(P1_hand, PC_hand):
  player_total = sum(P1_hand)
  opponent_total = sum(PC_hand)
  if player_total > 21:
    print(f"Your hand: {player_total}   Bust! You lose.")
  else:
    while opponent_total < twentyone - 4:
      # TODO: hit with a 'soft' 17
      deck_size = len(card_values)-1
      next_card = card_values[rn.randint(0, deck_size)]
      # if not statistical_impossibility:
      #   card_values.remove(next_card)
      PC_hand.append(next_card)
      opponent_total = sum(PC_hand)
      #print(opponent_total)
    if opponent_total > twentyone:
      print(f"Dealer's score: {opponent_total}    Bust! You win.")
    else:
      result = "You lose"
      if player_total > opponent_total:
        result = "You win"
      elif player_total == opponent_total:
        result = "It's a push.."
      print(f"Your score was {player_total}, {P1_hand} against the dealer's {opponent_total}, {PC_hand}. {result}.")



def play_hand(P1_hand):
  #print(f"Playing: {P1_hand}")
  total = sum(P1_hand)
  if total == 21:
    print("BlackJack! Congratulations! You win!")
    opponent_hand = PC_hand
  else:
    opponent_hand = hit_stand()
  return opponent_hand
      
def play_split_hand(split_hand, PC_hand):
  play_hand(split_hand)
  pass


### Begin ###

P1_hand = []
PC_hand = []

P1_hand.append(draw_card())
PC_hand.append(draw_card())
P1_hand.append(draw_card())
PC_hand.append(draw_card())

player_total = sum(P1_hand)
opponent_total = sum(PC_hand)
print(f"Your cards: {P1_hand}, current score: {player_total}\nComputer's first card: {PC_hand[0]}")


if P1_hand[0] == P1_hand[1]:
  split = input(f"Two {P1_hand[0]}s, will you split them? Type 'y' for yes, 'n' for no: ").lower()
else:
  split = 'n'

accepted = False
while not accepted:
  if split == 'y' or split == 'n':
    accepted = True
  else:
    split = input("That wasn't an accepted response, type 'y' or 'n': ")

if split == 'y':
  card = P1_hand[0]
  split_hand = [card]
  #P1_hand.remove(card)
  P1_hand.append(draw_card())
  split_hand.append(draw_card())
  PC_hand = play_hand(P1_hand)
  play_split_hand(split_hand, PC_hand)

if split == 'n':
  play_hand(P1_hand)




















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




  

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.






# All this would save a lot of time if we were to extend this program to accomodate additional players.
# deal_order = []
# players = 2
# for i in range (players*2):
#   if i % players == 0:
#     deal_order.append(PC_hand)
#   elif i % (players-1) == 0:
#     deal_order.append(P1_hand)
# print(f"Deal order: {deal_order}")

# ^^ The stipulation being that we would have to have the ability of passing by reference.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

