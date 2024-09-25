
import pgzrun
WIDTH = 600
HEIGHT = 500
a = Rect((100,100), (100, 800))

def draw():
    screen.clear()
    screen.fill("lightblue")
    screen.draw.circle((150,150),70,"red")
    screen.draw.filled_circle((250,250),100,"red")
    screen.draw.filled_rect((a), "red")




pgzrun.go()
