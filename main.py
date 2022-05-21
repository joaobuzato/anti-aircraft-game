import time
from turtle import Screen, Turtle
from cannon import Cannon

screen = Screen()

screen.setup(width=410, height=310)
screen.title("Anti-Aircraft")
bg_img = "img/bg.gif"
cannon_img = "img/cannon.gif"

screen.register_shape(bg_img)
bg_img = Turtle(shape=bg_img)
screen.register_shape(cannon_img)


cannon = Cannon()
cannon.shape(cannon_img)


screen.tracer(0)

game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()


screen.mainloop()