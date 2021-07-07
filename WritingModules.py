# Modules in Python are simply Python files with a .py extension. 
# The name of the module will be the name of the file. 
# A Python module can have a set of functions, classes or variables defined and implemented


# "game.py" will implement the game. 
# It will use the function "draw_game" from the file "draw.py", or in other words, the "draw" module, that implements the logic for drawing the game on the screen.

# Modules are imported from other modules using the import command. the game.py script may look something like this:

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

# In this example, the game module imports the draw module, which enables it to use functions implemented in that module. The main function would use the local function play_game to run the game, and then draw the result of the game using a function implemented in the draw module called draw_game. To use the function draw_game from the draw module, we would need to specify in which module the function is implemented, using the dot operator. To reference the draw_game function from the game module, we would need to import the draw module and only then call draw.draw_game(). 