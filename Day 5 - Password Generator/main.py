#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

'''
Masking input - pip install pwinput
https://stackoverflow.com/questions/27631629/masking-user-input-in-python-with-asterisks#:~:text=Unlike%20getpass.getpass%20%28%29%20%28which%20is%20in%20the%20Python,%3E%3E%3E%20pwinput.pwinput%20%28mask%3D%27X%27%29%20%23%20Change%20the%20mask%20character.

Masking I/O  - pip install stdiomask
https://newbedev.com/masking-user-input-in-python-with-asterisks#:~:text=Unlike%20getpass.getpass%20%28%29%20%28which%20is%20in%20the%20Python,%3E%3E%3E%20stdiomask.getpass%20%28mask%3D%27X%27%29%20%23%20Change%20the%20mask%20character.
'''

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letter_choices = len(letters)
number_choices = len(numbers)
symbol_choices = len(symbols)

password = []
# We could also have put just simply...
# password = ""
for i in range(0, nr_letters):
  picked_letter = random.randint(0, letter_choices-1)
  password.append(letters[picked_letter])

for i in range(0, nr_symbols):
  picked_symbol = random.randint(0, symbol_choices-1)
  password.append(symbols[picked_symbol])

for i in range(0, nr_numbers):
  #picked_number = random.randint(0, number_choices-1)
  #password.append(numbers[picked_number])
  picked_number = random.choice(numbers)
  password.append(picked_number)
  # Or.. if we used a string... 
  #password += picked_number 

'''  Output
password = ''.join(password)
print(password)
'''

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
total_chars = nr_letters + nr_symbols + nr_numbers
scrambled_password = []
for i in range(0, total_chars):  # 0 is assumed here, and totally unnecessary. range(total_chars) is equally valid.
  next_index = random.randint(0, total_chars-1-i)
  #print(next_index)
  next_char = password[next_index]
  scrambled_password.append(next_char)
  # we can actaully concatenate here to if we so choose
  #scrambled_password = scrambled_password + next_char
  
  password.remove(next_char)
  #Note! There's no method for removing at an index.
  # This is fine for our purposes because threre's
  # no context between char placing in this case.

'''Much simpler than the above for loop...
random.shuffle(password)
  accomplishes the same thing
'''
f = open("mypassword.txt", "w")

password = ''.join(scrambled_password)
f.write(password + "\n")
f.close()
'''If the file doesn't close, the file doesn't save!'''

password = ""
for i in range(0, total_chars):
  password += '*'

print(password)

r = open("mypassword.txt", "r")
#print(r.read())
r.close()

#Next level - Mask it in the display (use asterix or dot chars)[or octothorpes? 🤔]
# Maintain the ability to copy it without losing the ability to verify with it.
# Store the unmasked version in a file for later access.

'''
Looks like we can write files in the bash environment, but can not read from them.
'''