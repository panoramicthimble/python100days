from replit import clear
#HINT: You can call clear() to clear the output in the console.
clear()

#User specifications
spec = False
'''
We can reset to the requested parameters by setting this to True
'''

from art import logo
print(logo)
bids_index = {}

next_bidder = True
while next_bidder:
  name = input("What is your name?: ")
  bid = input("What is your bid?: $")
  bids_index[name] = int(bid)
  
  next = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  while(next!='yes'and next!='no'and next!='y'and next!='n'):
    next = input("That wasn't an option. Please type 'yes' or 'no'\n.").lower()

  if(next=='no'or next=='n'):
    next_bidder = False
  clear()
  print(logo)

max = -9999999
paid = 0

winner = ""
for bid in bids_index:
  val = bids_index.get(bid)
  #Testing: prints list
  #print(f"bid is {bid}:{val}")
  if val > paid:
    if val < max:
      paid = val +1
  if val > max:
    paid = max+1
    max = val
    winner = bid
  if not spec:  
    print(f"The winner is {winner} with a bid of ${paid}")
# Specification code
if spec:
  print(f"The winner is {winner} with a bid of ${max}")