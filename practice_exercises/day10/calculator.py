#Calculator

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number?: "))
continue_calculating = True

while continue_calculating:

  for operation in operations:
      print(operation)

  operation_symbol = input("Pick an operation from the line above: ")

  num2 = int(input("What's the next number?: "))

  operation_function = operations[operation_symbol]

  answer = operation_function(num1, num2)

  print(f"{num1} {operation_symbol} {num2} = {answer}")

  next_step = input(f"Type 'y' to continue calculating with {answer} or 'n' to exit.\n")

  if next_step == 'y':
      num1 = answer
  elif next_step == 'n':
      continue_calculating = False
      print('Goodbye.')