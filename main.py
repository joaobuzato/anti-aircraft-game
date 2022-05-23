import time
from turtle import Screen
from cannon import Cannon
from missile_manager import MissileManager
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=410, height=310)
screen.title("Anti-Aircraft")
bg_img = "img/bg.gif"
screen.bgpic(bg_img)

cannon = Cannon(screen)
missile_manager = MissileManager(screen)
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="a", fun=cannon.turn_left)
screen.onkey(key="d", fun=cannon.turn_right)
screen.onkey(key="k", fun=cannon.shoot)

screen.tracer(0)

game_is_on = True

while game_is_on:
    time.sleep(0.03)
    screen.update()
    cannon.move_shots()
    missile_manager.missile_bombing()
    missile_manager.move_missiles()
    if missile_manager.hit_the_ground():
        scoreboard.game_over()
        game_is_on = False

    for shot in cannon.shots:
        if missile_manager.detect_colision(shot):
            scoreboard.point()
            cannon.shot_manager.explode(shot)


screen.exitonclick()