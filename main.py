import time
from turtle import Screen
from cannon import Cannon
from missile_manager import MissileManager

screen = Screen()

screen.setup(width=410, height=310)
screen.title("Anti-Aircraft")
bg_img = "img/bg.gif"
screen.bgpic(bg_img)

cannon = Cannon(screen)
missile_manager = MissileManager(screen)

screen.listen()
screen.onkey(key="a", fun=cannon.turn_left)
screen.onkey(key="d", fun=cannon.turn_right)
screen.onkey(key="k", fun=cannon.shoot)

screen.tracer(0)

game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    cannon.move_shots()
    missile_manager.missile_bombing()
    missile_manager.move_missiles()
    for shot in cannon.shots:
        if missile_manager.detect_colision(shot):
            cannon.shot_manager.explode(shot)

screen.exitonclick()