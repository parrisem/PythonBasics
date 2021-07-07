# NUMBERS
myint = 7
print(myint)

# DEFINE A FLOATING POINT NUMBER
# first way
myfloat = 7.0
print(myfloat)

# second way
myfloat = float(7)
print(myfloat)


# STRINGS
# first way
mystring = 'hello'
print(mystring)
# second way
mystring = "hello"
print(mystring)

mystring = "Don't worry about apostrophes"
print(mystring)

# OTHER USES OF NUMBERS AND STRINGS
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# assigning more than one variable at the same time
a, b = 3, 4
print(a,b)

# you can't mix operators between numbers and strings (the line below will not work)
# print(one + two + hello)


# Exercise
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
  print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
  print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
  print("Integer: %d" % myint)