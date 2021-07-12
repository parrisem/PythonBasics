# WRITING MODULES
# Modules in Python are simply Python files with a .py extension. 
# The name of the module will be the name of the file. 
# A Python module can have a set of functions, classes or variables defined and implemented


# "game.py" will implement the game. 
# It will use the function "draw_game" from the file "draw.py", or in other words, the "draw" module, that implements the logic for drawing the game on the screen.

# Modules are imported from other modules using the 'import' command. the 'game.py' script may look something like this:

# game.py
# import the draw module
import draw

def play_game():
    ...

def main():
    result = play_game()
    draw.draw_game(result)

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()


# The draw module may look something like this:
# draw.py

def draw_game():
    ...

def clear_screen(screen):
    ...

# The 'game' module imports the 'draw' module and enables it to use functions implemented in that module. 
# The 'main' function uses the local function 'play_game' to run the game, then draw the result of the game using a function implemented in the 'draw' module called 'draw_game'. 
# To use the function 'draw_game' from the 'draw' module, you need to specify which module the function is implemented, using the dot operator. 
# To reference the draw_game function from the game module, we would need to import the draw module and only then call 'draw.draw_game()'.
# When the 'import draw' directive will run, the Python interpreter will look for a file in the directory which the script was executed from, by the name of the module with a '.py' suffix
# so in this case it will try to look for 'draw.py'. If it finds the file it will import it. If it doesn't it will continue to look for built-in modules.

# IMPORTING MODULE OBJETCS TO THE CURRENT NAMESPACE
# You can also import the function 'draw{_game' directly into the main script's namespace using the 'from' command.

# game.py
# import the draw module
from draw import draw_game

def main():
    result = play_game()
    draw_game(result)

# The 'draw_game' doesn't precede with the name of the module it is imported from as we have already specified the module name in the 'import' command
# Using this notation is easier to use functions inside the current module because it isn't necessary to specify the module the function comes from. 
# However, any namespace cannot have two objects with the exact same name, so the 'import' command may replace an existing object in the namespace.

# IMPORTING ALL OBJECTS FROM A MODULE
# Use the 'import *' command to import all objects from a specific module

# game.py
# import the draw module
from draw import *

def main():
    result = play_game()
    draw_game(result)

# This notaion ius shorter and doesn't require yo to specify which objects you wish to import from the module.

# CUSTOM IMPORT NAME
# You can load modules under any name. useful when you want to import a module conditionally to use the same name in the rest of the code.
# if you have two 'draw' modules with slightly different names - you can do this:

# game.py
# import the draw module
if visula_mode:
    # in visual mode, we draw using graphics
    import draw_visual as draw
else:
    # in textual mode, we print out text
    import draw_textual as draw

def main():
    result = play_gamne()
    # this can either be visual or textual depending on visual_mode
    draw.draw_game(result)


# MODULE INITIALIZATION
# modules are only initialized once even if your code imports the same module again. so local variables in the module act as a "singleton" - they are initialized only once.

# draw.py

def draw_game():
    # when clearing the screen we can use the main screen object initialized in this module
    clear_screen(main_screen)
    ...

def clear_screen(screen):
    ...

class Screen():
    ...

# initialize mani_screen as a singleton
main_screen = Screen()

# EXTENDING MODULE LOAD PATH
# You can tell the Python interpreter where to look for modules, aside from the default (local directory and built-in modules). You can use the environment variable 'PYTHONPATH' to specify additional directories to look for modules in:

PYTHONPATH = /foo python game.py

#  This will execute 'game.py' and will enable the script to load modules from the 'foo' directory as well as the local directory.
# another method is tyo use 'sys.path.append' function. can be executed before running an 'import' command:
sys.path.append("/foo") 
# This adds the 'foo' directory to the list of paths to look for modules in as well.

# EXPLORE BUILT-IN MODULES
# You can find a full list of built-in modules in the Python standard library here 'https://docs.python.org/3/library/'
# Important functions are 'dir' and 'help'. 
# The 'urllib' module enable us to create read data from URLs. Just 'import' the module:

# import the library 
import urllib

# use it
urllib.urlopen()

# you can look for which functions are implemented in each module by using the dir function:
>>> import urllib
>>> dir(urllib)

# when you find the function in the modyule that you want to use, you can read about it in more detail using the 'help' function, inside the Python interpreter
help(urllib.urlopen)

# WRITING PACKAGES
# Packagesare namespace which contain multiple packages and modules themselves. they are just directories, but with a twist.
# Each package in Python is a directory which MUST contain a special file called '__init_.py', which can be empty file and indicates that the directory it contains is a Python package, so it can be imported the same a module can be imported.
# If you create a directory called 'foo', which marks the package name, we can then create a module inside that package called 'bar'. We also must not forget to add the '__init__.py' file inside the 'foo' directory.

# To use the 'bar' module, you can import it two ways:
import foo.bar
from foo import bar

# '__init__.py' file can also decide which modules the package exports as the API, while keeping other modules internal, by overriding the '__all__' variable, like so:
__init__.py
__all__ = ["bar"]

# EXERCISE

import re

find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))

