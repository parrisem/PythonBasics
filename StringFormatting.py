# C-style string formatting using '%' operator e.g. "%s" and "%d"
# This prints out "Hello, John!"
name = "Parris"
print("Hello, %s!" % name)

# using two or more argument specifiers
age = 22
print("%s is %d years old." % (name, age))

# Any object which is not a string can be formatted using the %s operator as well.
mylist = [1,2,3]
print("A list: %s" % mylist)

# Basic argument specifiers to know

# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)

# Exercise
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)