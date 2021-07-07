# Python uses boolean logic to evaluate conditions. 
# The boolean values True and False are returned when an expression is compared or evaluated
# assignment is with '=' and comparison is with '==' (eqaul to) or '!=' (not equal to)
x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

# The "and" and "or" boolean operators allow building complex boolean expressions
name = "Parris"
age = 22
if name == "Parris" and age == 22:
  print("Your name is Parris, and you are also 22 years old.")
if name == "Parris" or name == "Kelvin":
  print("Your name is either Parris or Kelvin.")

# The "in" operator could be used to check if a specified object exists within an iterable object container
if name in ["Parris", "Kelvin"]:
  print("Your name is either Parris or Kelvin.")

# indentation is used to define blocks of code instaed of brackets
statement = False
another_statement = True
if statement is True:
  # do something
  pass
elif another_statement is True: # else if
  # do something else
  pass
else:
  # do another thing
  pass

x = 2
if x == 2:
  print("x equals two!")
else:
  print("x does not equal to two.")

# A statement is evaulated as true if one of the following is correct: 
# 1. The "True" boolean variable is given, or calculated using an expression, such as an arithmetic comparison. 
# 2. An object which is not considered "empty" is passed.
# examples for objects which are considered as empty: 
# 1. An empty string: "" 
# 2. An empty list: [] 
# 3. The number zero: 0 
# 4. The false boolean variable: False

# the "is" operator does not match the values of the variables, but the instances themselves
x = [1,2,3]
y = [1,2,3]
print(x == y) # prints out True
print(x is y) # prints out False

# "not" before a boolean expression inverts it
print(not False) # prints out True
print((not False) == (False)) # prints out True

print("\nEXERCISE")
# change this code
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")