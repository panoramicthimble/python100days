# We're up to 3 copies of this project. main-2 is closest to the provided solution. This one was the initial attempt.
# start-1 was intended as a 'cleanest version'

from replit import clear
clear()

from art import logo
print(logo)

def get_input():
  operandA = float(input("What's the first number?: "))
  print("+")
  print("-")
  print("*")
  print("/")
  operator = input("Pick an operation: ")
  operandB = float(input("What's the next number?: "))
  return {"opA": operandA, "opB": operandB, "op": operator}
  
def get_next_input():
  operator = input("Pick an operation: ")
  operandB = float(input("What's the next number?: "))
  return {"opB": operandB, "op": operator}

def op(operandA, operandB, operator):
  valid = False
  while not valid:
    valid = True
    if operator == '+':
      result = operandA + operandB
    elif operator == '-':
      result = operandA - operandB
    elif operator == '*':
      result = operandA * operandB
    elif operator == '/':
      result = operandA / operandB
    elif operator == '^':
      result = operandA
      for i in range(int(operandB)-1):
        result *= operandA
    else:
      valid = False
      operator = input("That wasn't one of the options, please enter '+', '-', '*', or '/'\n")
      op(operandA, operandB, operator)
  print(f"{operandA} {operator} {operandB} = {result}")
  return result


finished = False
while not finished:
  inputs = get_input()
  operandA = inputs.get("opA")
  operandB = inputs.get("opB")
  operator = inputs.get("op")
  
  result = op(operandA, operandB, operator)

  # More calculations to be carried out 
  answered = False
  while not answered:
    running_calc = input(f'''Type 'y' to continue calculating with {result}, or type 'n' to exit or start a new calculation: ''').lower()
    if running_calc == 'n':
      complete = input("Did you have another operation to perform? ")
      while (complete!='y'and complete!='n'):
        complete = input("That wasn't one of the options, please type 'y' or 'n'.\n").lower()
      if(complete=='n'):
        finished = True
        answered = True
        clear()
        print(f"{operandA} {operator} {operandB} = {result} and that's my final answer.")
      else:
        clear()
        print(logo)
        answered = True
    elif running_calc == 'y':
      next_input = get_next_input()
      
      inputs.update(next_input)
      operandB = inputs["opB"]
      operator = inputs["op"]

      result = op(result, operandB, operator)