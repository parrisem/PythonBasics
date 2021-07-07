# objects are an encapsulation of variables and functions into a single entity
# objects get their variables and functions from classes
# classes are a template to create objects
class MyClass:
  variable = "blah"

  def function(self):
    print("This is a message inside the class.")

# to assign the class to an object 
myobjectx = MyClass()

# to access the variable inside of the newly created object "myobjectx"
myobjectx.variable

# prints out "blah"
print(myobjectx.variable)

# can create multiple different objects that are of the same class(have the same variables and functions defined). 
# but, each object contains independent copies of the variables defined in the class
myobjecty = MyClass()
myobjecty.variable = "yackity"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)

# to access a function inside of an object you use notation similar to accessing a variable
myobjectx.function()

# Exercise
print("\nEXERCISE")
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

car1 = Vehicle()
car1.name = "Fer"
car1.kind = "convertable"
car1.color = "red"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())