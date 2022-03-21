# # Review: 
# # Create a function called greet().
# # Response to the question.
# def greet(greeting, location):
# # # Write 3 print statements inside the function.
#   greeting = input('Please enter your name?\n').capitalize()
#   location = input('What state do you live in?\n').capitalize()
#   print(f"Hi! {greeting}.")
#   print(f'{greeting} is a very nice name.')
#   print(f'Today we will be learning about function {greeting}.')
#   print(f"How's the weather in {location}?")
# # # Call the greet() function and run your code.
# greet('greeting', 'location')



# This way is a little less interactive.
def greet_with_parameter(name, location):
# Write 3 print statements inside the function.
  print(f"Hi! {name}.")
  print(f'{name} is a very nice name.')
  print(f'Today we will be learning about function {name}.' )
  print(f"How's the weather in {location}?")
# Call the greet() function and run your code.
# A name has to be entered or a error will be thrown.
# Using keyword arguments.
greet_with_parameter(name = 'Jack', location = 'Florida')
