# Review: 
# Create a function called greet().
# Response to the question.
# def greet():
# # Write 3 print statements inside the function.
#   greeting = input('Please enter your name?\n').capitalize()
#   print(f"Hi! {greeting}.")
#   print(f'{greeting} is a very nice name.')
#   print(f'Today we will be learning about function {greeting}.' )
# # Call the greet() function and run your code.
# greet()

# This way is a little less interactive.
def greet_with_parameter(name):
# Write 3 print statements inside the function.
  print(f"Hi! {name}.")
  print(f'{name} is a very nice name.')
  print(f'Today we will be learning about function {name}.' )
# Call the greet() function and run your code.
# A name has to be entered or a error will be thrown.
greet_with_parameter("Jack")
