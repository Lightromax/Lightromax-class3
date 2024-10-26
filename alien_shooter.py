import pgzrun
WIDTH=500
HEIGHT=465

alien=Actor("alien")
   #screen.draw.filledcircle("lime")

TITLE="Alien blaster"
def draw():
    screen.clear()
    screen.fill("blue")
    screen.draw.text("Hello try my game",(300,50))
    alien.draw()

pgzrun.go()