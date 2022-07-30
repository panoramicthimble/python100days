#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.\n")
bill = float(input("What was the total bill? $"))
covers = int(input("\nHow many people to split the bill? "))
tip = int(input("\nWhat percentage tip would you like to give? 10, 12, or 15? "))

# Perform required math and data handling
tipped_bill = bill * ( 1 + tip/100)
per_person = tipped_bill / covers

total = round(per_person, 2)
# The problem here is that a result of $33.60 displays as $33.6

''' This stores the format string (and nothing else) as a string.
total = ('%.2f'.format(total))
print(f"\nEach person should pay: ${total}")
'''

#So does this
#print("\nEach person should pay: $" + '%.2f'.format(total))

''' Same problem as before
total += 0.001
total = round(total, 2)
print(f"\nEach person should pay: ${total}")
'''

# This one works.
# Thanks grant zukowski
#  https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
total = format(total, '.2f')
print(f"\nEach person should pay: ${total}")

''' (Given Solution to the formatting problem)
total = "{:.2f}".format(per_person)
# Note the addition of curly braces here.
'''
