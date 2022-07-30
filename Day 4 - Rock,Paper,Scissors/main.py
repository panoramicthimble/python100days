rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random as r

choices = [rock, paper, scissors]

def PC_move():
  move = r.randint(0,2)
  move = move//1
  print("Computer chose:\n")
  print(choices[move])
  return move

def player_move():
  move = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
  #if(type(move) == class 'str'):
  #if(isinstance(move, str) and (move=='0' or move=='1' or move=='2'):
  move = int(move)
  if move>=0 and move <=2:
    print(choices[move])
  else:
    print("That wasn't an option!")
    exit()
  # else:
  #   print(f"Detected {type(move)}")
  #   print("That wasn't an option!")
  #   exit()      
  return move

def play_game():
  move = player_move()
  PC = PC_move()
  message = "You win"
  if move < 2:
    if PC > move:
      message = "You lose"
  elif move == 2:
    if PC == 0:
      message = "You lose"
  
  if PC == move:
    message = "It's a draw"
  print(message)

play_game()