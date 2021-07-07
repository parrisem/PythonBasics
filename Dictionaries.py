# dictinaries is a data type similar to arrays, but work with keys and values instead of indexes
# each value stored in a dictionary can be accessed using a key which can be any type ofg object (string, number, list, etc)
phonebook = {}
phonebook["Parris"] = 938477566
phonebook["Jade"] = 938377264
phonebook["Kat"] = 947662781
print(phonebook)

# another way to initialise a dictinary
phonebook = {
    "Parris" : 938477566,
    "Jade" : 938377264,
    "Kat" : 947662781
}
print(phonebook)

# you can iterate over dictionaries just like lists
# a dictionary, unlike a list, does not keep the order of the values stored in it. To iterate over key value pairs do this:
for name, number in phonebook.items():
  print("Phone number of %s is %d" % (name,number))

# To remove a specified index, use either one of the following notations:
del phonebook["Jade"]
print(phonebook)

# or

phonebook.pop("Kat")
print(phonebook)

# Exercise
print("\nEXERCISE")
phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
phonebook["Jake"] = 938273443
del phonebook["Jill"]
# testing code
# print(phonebook)
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")  