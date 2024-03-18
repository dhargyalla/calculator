#calculator
from art import logo
#add
def add(n1, n2):
  return n1 + n2
#subtract
def sub(n1, n2):
  return n1 - n2
#multiply
def mul(n1, n2):
  return n1 * n2
#divide
def div(n1, n2):
  return n1 / n2

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  operations = { "+": add, "-": sub, "*": mul, "/": div}
  for symbol in operations:
    print(symbol)
  
  should_continue = False
  while not should_continue:
    operation_symbols = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number?: "))
    operation_function = operations[operation_symbols]
    answer = operation_function(num1, num2)
    print(f"{num1} {operation_symbols} {num2} = {answer}")
    
    respond = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit")
    if respond == "y":
      num1 = answer
    else:
      should_continue = True
      calculator()

calculator()


    
  







 
  
      




    

