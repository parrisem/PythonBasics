# lists are simple arrays. they can contain any type of variable, and they can contain as many variables as you wish. Lists can also be iterated over in a very simple manner.
mylist = []
mylist.append(1)
mylist.append(2) 
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3
# prints outs 1,2,3
for x in mylist:
  print(x)

# accessing an index that doesn't exist throws an exception (error)

mylist = [1,2,3]
print(mylist[0])

# Exercise
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")
second_name = names[1]

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)