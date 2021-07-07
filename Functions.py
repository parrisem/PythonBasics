#  a convenient way to divide your code into useful blocks, allowing us to order our code, make it more readable, reuse it and save some time. 
# functions are defined using "def" followed by the function name
def my_func():
  print("Hello this is my first function")
# functions can have arguments (variables passed from the caller to the function)
def my_func_with_args(username, greeting):
  print("Hello, %s, from my function!, I wish you %s" % (username, greeting))
# function can return a value to the caller using "return"
def sum_two_numbers(a,b):
  return a + b

#  you call functions by writing the function's name followed by "()" and put the required arguments in the brackets
# print(a simple greeting)
my_func()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_func_with_args("Parris M", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(6,9)
print(x)

# Exercise
print("\nEXERCISE")
def list_benefits():
  return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together" 

def build_sentence(benefit):
  # for i in benefit:
  #   print(i + "is a benefiut of functions!")
  return "%s is a benefit of functions!" % benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()
