# Input
#
# [4,5,6]
# Expected output
#
# You called a_function(4, 5, 6)
# It returned: 120

inputs = eval(input("Input a list of three numbers: "))
# TODO: Create the logging_decorator() function 👇
def logging_decorator(func):
  def wrapper(*args):
    print(args)
    print( f"You called {func.__name__}{args}")
    result = func(args[0],args[1],args[2])
    print(f"It returned: {result}")
  return wrapper

# TODO: Use the decorator 👇
@logging_decorator
def a_function(a, b, c):
  return a * b * c

a_function(inputs[0], inputs[1], inputs[2])