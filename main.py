import time
from turtle import Screen
from cannon import Cannon

screen = Screen()

screen.setup(width=410, height=310)
screen.title("Anti-Aircraft")
bg_img = "img/bg.gif"
screen.bgpic(bg_img)
cannon_img = "img/cannon.gif"
cannon_img_left_45 = "img/cannon-45.gif"
cannon_img_right_45 = "img/cannon45.gif"

screen.register_shape(cannon_img)
screen.register_shape(cannon_img_left_45)
screen.register_shape(cannon_img_right_45)


cannon = Cannon()
cannon.shape(cannon_img)


def cannon_turn_left():
    cannon.turn_left()
    if cannon.heading() == 90:
        cannon.shape(cannon_img)
    else:
        cannon.shape(cannon_img_left_45)


def cannon_turn_right():
    cannon.turn_right()
    if cannon.heading() == 90:
        cannon.shape(cannon_img)
    else:
        cannon.shape(cannon_img_right_45)


screen.listen()
screen.onkey(key="a", fun=cannon_turn_left)
screen.onkey(key="d", fun=cannon_turn_right)
screen.onkey(key="k", fun=cannon.shoot)

screen.tracer(0)

game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()


screen.exitonclick()