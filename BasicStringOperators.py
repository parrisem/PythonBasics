# can be defined as anything between quotes
astring = "Hello world!"
# can also use single quotes to assign a string
astring2 = 'Hello world!'

# use double quotes if the string itself uses single quotes 
print("single quotes are ' '")

# prints out 12, because "Hello world!" is 12 characters long, including punctuation and spaces
print("Length of string: %d" % len(astring))

# prints out 4, because the location of the *first* occurrence of the letter "o" is 4 characters away from the first character (index starts at 0 in poyton)
print("Index of the first 'o' in the string: %d"% astring.index("o"))

# counts all the instances of 'l' in the string. therfore should be 3

print("There are %d instances of 'l'." % astring.count("l"))

# prints a slice of the string, starting at index 3, and ending at index 6
print("Characters from index 3 to 6: %s" % astring[3:7])
# if you just have one number in the brackets, it will give you the single character at that index
print("Character at index 3: %s" % astring[3])
# if you leave out the first number but keep the colon, it will give you a slice from the start to the number you left in
print("Charactes from index 0 to 6: %s" % astring[:7])
# if you leave out the second number, it will give you a slice from the first number to the end
print("Charactes from index 3 to the end: %s" % astring[3:])
# you can even put negative numbers inside the brackets. They are an easy way of starting at the end of the string instead of the beginning. This way, -3 means "3rd character from the end"
print(f"Different types of indexing: {astring[-3]}{astring[3:7:2]}{astring[3:7]}{astring[3:7:1]}")
# prints the characters of string from 3 to 7 skipping one character [start:stop:step] 
# print(astring[3:7:2])
# prodice the same output
# print(astring[3:7])
# print(astring[3:7:1])
# can easily reverse a string like this
print("String in reverse: %s" % astring[::-1])
# make a new string with all letters converted to uppercase and lowercase, respectively
# print(astring.upper())
print("String in caps: %s" % astring.upper())
# print(astring.lower())
print("String in lowercase: %s" % astring.lower())

# used to determine whether the string starts with something or ends with something, respectively
# print(astring.startswith("Hello"))
print("Does the string start with 'Hello'? %s" % astring.startswith("Hello"))
# print(astring.endswith("asdfasdfasdf"))
print("Does the string end with 'asdfasdfasdf'? %s" % astring.endswith("asdfasdfasdf"))

# Exercise
print()
print("EXERCISE")
s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))
# Firstoccurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))
# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))