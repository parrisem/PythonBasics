# for loops iterate over a given sequence for a while
print("For loops")
primes = [2,3,5,7]
for prime in primes:
  print(prime)

# For loops can iterate over a sequence of numbers using the "range" and "xrange" functions. 
# The difference between range and xrange is that the range function returns a new list with numbers of that specified range, whereas xrange returns an iterator, which is more efficient

# prints out the numbers 0,1,2,3,4
for x in range(5):
  print(x)

# prints out 3,4,5
for x in range(3,6):
  print(x)

# prints out 3,5,7
for x in range(3,8,3):
  print(x)

print("\nWhile loops")
# while loops repeat as long as the certain boolean condition is met
# prints out 0,1,2,3,4
count = 0
while count < 5:
  print(count)
  count += 1 # this is the same as count = count + 1

# "break" and "continue" statements
# break is used to exit a for loop or a while loop 
# continue is used to skip the current block and return the "for" or "while" statement
# print out 0,1,2,3,4
print("\nBreak and Continue statements")
while True:
  print(count)
  count += 1
  if count >= 5:
    break

# prints out only odd numbers - 1,3,5,7,9
for x in range(10):
  # check if x is even
  if x % 2 == 0:
    continue
  print(x)

# "else" in "for" and "while" loops
# When the loop condition of "for" or "while" statement fails then code part in "else" is executed. 
# If a break statement is executed inside the for loop then the "else" part is skipped. 
# Note that the "else" part is executed even if there is a continue statement.
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"
print("\nElse")
while(count <5):
  print(count)
  count += 1
else:
  print("count value reached %d" %(count))

# prints out 1,2,3,4
for i in range(1,10):
  if(i % 5 == 0):
    break
  print(i)
else:
  print("this is not printed becasue for loop is terminated because of break but not due to fail in condition")




# Exercise
print("\nEXERCISE")
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for n in numbers:
  if n == 237:
    break
  if n % 2 == 1:
    continue
  print(n)