import pgzrun
from random import randint

apple = Actor("apple")

# Draws The Apple With Valid Coords (x,y) 
def place_apple():
	apple.x = randint(10, 800)
	apple.y = randint(10, 600)

def draw():
	screen.clear()
	apple.draw()

# Responds to user input
def on_mouse_down(pos):
	if apple.collidepoint(pos):
		print("Good shot!")
		place_apple()
	else:
		print("You missed!")
		quit()
place_apple()
pgzrun.go()
