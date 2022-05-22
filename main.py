import time
from turtle import Screen
from cannon import Cannon

screen = Screen()

screen.setup(width=410, height=310)
screen.title("Anti-Aircraft")
bg_img = "img/bg.gif"
screen.bgpic(bg_img)



cannon = Cannon(screen)


screen.listen()
screen.onkey(key="a", fun=cannon.turn_left)
screen.onkey(key="d", fun=cannon.turn_right)
screen.onkey(key="k", fun=cannon.shoot)

screen.tracer(0)

game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()


screen.exitonclick()