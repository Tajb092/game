my_character = Actor("Akbar")
my_character.pos = 100, 50

WIDTH = 500
HEIGHT = my_character.height + 20

def draw():
    screem.fill((0,0,0))
    screen.clear()
    my_character.draw()
