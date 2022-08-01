#from replit import clear
from os import system
windows = True
if windows == False:
    from os import name
from random import randint
from game_data import data

items = len(data)

def clear():
    if windows == False:#os.name == 'nt'
        _ = system('clear')
    else:   #os.name == 'posix'
        _ = system('cls')

def refresh():
    clear()
    print(logo)


# // select two options to check followers for
def set_choices():
    optionA = randint(0, items - 1)
    optionB = randint(0, items - 1)
    # generates new ones until the values are distinct
    while optionA == optionB:
        optionB = randint(0, items - 1)
    return [optionA, optionB]


def display_choices(indexA, indexB):
    resolved = False
    while not resolved:
        optionA = data[indexA]
        keyA = optionA['name']
        valA = optionA['follower_count']
        descA = optionA['description']
        natA = optionA['country']
        optionB = data[indexB]
        keyB = optionB['name']
        valB = optionB['follower_count']
        descB = optionB['description']
        natB = optionB['country']
        if valA == valB:
            set_choices()
            continue
        resolved = True
        if valA > valB:
            answer = 'A'
        elif valB > valA:
            answer = 'B'
    print(f"Compare A: {keyA}, {descA}, from {natA}.")
    print(vs)
    print(f"Against B: {keyB}, {descB}, from {natB}.")
    return answer


def set_round():
    AB = set_choices()
    answer = display_choices(int(AB[0]), int(AB[1]))
    return answer


def guess(streak, answer):
    guess = str(input("Who has more followers? Type 'A' or 'B': ").title())
    while guess != "A" and guess != "B":
        guess = input("That choice wasn't recognized, enter 'A' or 'B': ").title()
    if guess == answer:
        refresh()
        streak += 1
        print(f"You're right! Current score: {streak}.")
    else:
        # refresh()
        print(f"Sorry, that's wrong. Final score: {streak}")
        streak = -1
    return streak


'''
keyA = list(data.values())[optionA]['name']
valA = list(items.values())[optionA]['follower_count']
descA= list(items.values())[optionB]['description']
natA = list(items.values())[optionB]['country']

keyB = list(items.values())[optionB]['name']
valB = list(items.values())[optionB]['follower_count']
descB= list(items.values())[optionB]['description']
natB = list(items.values())[optionB]['country']
# None of this works.
'''
# This works fine though.
# print(data[optionA])
'''
The reason being... ?
'''

from art import logo
from art import vs

refresh()
streak = 0
while streak > -1:
    # refresh()
    answer = set_round()
    streak = guess(streak, answer)



