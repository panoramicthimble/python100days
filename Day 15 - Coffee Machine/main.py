MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

currencies = {
  "quarters":  .25,
  "dimes":    0.10,
  "nickles":  0.05,
  "pennies":  0.01,
}


def deminish_stores(menu_item, supplies):
  for ingredient in supplies:
    if ingredient in menu_item["ingredients"]:
      stocked = supplies[ingredient]
      required = menu_item["ingredients"][ingredient]
      # print(required)
      # print(stocked)
      if stocked >= required:
        stocked -= required
        supplies[ingredient] = stocked
      else:
        mise_en_place = list(supplies.keys())
        dry = mise_en_place.index(ingredient)
        missing_ingredient = mise_en_place[dry]
        print(f"Not enough {missing_ingredient}")

def order():
  beverage_choices = "("
  for item in MENU:
    beverage_choices += item +"/"
  beverage_choices = beverage_choices[:-1] + ")"
  
  selection = input(f"What would you like? {beverage_choices}: ")
  due = 0
  #Overly complicated saftey check
  for choice in MENU:
    if choice == selection:
      due = MENU[choice]["cost"]
  if due == 0:
    print("Sorry, that wasn't an option.")
  
  print("Please insert coins.")
  
  total = 0
  for money in currencies:
    add = int(input(f"How many {money}?: "))
    add *= currencies.get(money)
    total += add
  
  total_output = "${:,.2f}".format(total)
  print(f"You've paid {total_output}")
  if total > due:
    change = total - due
    change_output = "${:,.2f}".format(change)
    print(f"Your change: {change_output}")
    deminish_stores(MENU[choice], resources)
  else:
    print("Sorry, not enough money")
  
  
def get_another(satiated):
  thirsty = input("Would you like to order another one?").lower()
  if(thirsty != 'y' and thirsty != 'n'):
    print("That wasn't an option, please enter 'y' or 'n'")
    get_another(satiated)
    #return True
    '''If we enter the safety clause...
    the next choice either autocompletes with the return
    or skips an input without it
    '''
  elif(thirsty == 'n'):
    satiated = True
    return satiated
    

satiated = False

while not satiated:
  order()
  satiated = get_another(satiated)