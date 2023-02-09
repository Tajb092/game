my_character = Actor("akbar-fighting stance")
my_character.pos = 100, 50

WIDTH = 500
HEIGHT = my_character.height + 20

def draw():
    screen.fill((221,221,221))
    screen.clear()
    my_character.draw()

def update():
    my_character.left += 2
    if my_character.left > WIDTH:
        my_character.right = 0

def on_mouse_down(pos):
    if my_character.collidepoint(pos):
        print("hi you click!")
    else:
        print("not cool dude!")


