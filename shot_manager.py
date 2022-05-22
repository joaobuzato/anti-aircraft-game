from turtle import Turtle
from shot import Shot

shots = []

class ShotManager:
    def __init__(self):
        self.shot_speed = 10


    def shoot(self, screen, heading):
            shot = Shot(screen, heading)
            shots.append(shot)
            return shots

    def move_shots(self):
        for shot in shots:
            if shot.xcor() < -210 or shot.xcor() > 210 or shot.ycor() > 320:
                shots.remove(shot)
                del shot
            else:
                shot.forward(self.shot_speed)

    def explode(self, shot):
        shot.goto(500, 500)
        shots.remove(shot)
        del shot
