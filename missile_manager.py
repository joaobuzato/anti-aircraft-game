import random
from turtle import Turtle
from missile import Missile

headings =[270]
start_pos = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 215, 230, 245, 0, -15, -30, -45, -60, -75, -90, -105, -120, -135, -150, -165, -180, -195, -210, -215, -230, -245]

missiles = []

class MissileManager:
    def __init__(self, screen):
        self.missile_speed = 4
        self.screen = screen

    def missile_bombing(self):
        bombing = random.randint(0, 5) == 3
        if bombing:
            self.bomb(random.choice(headings), random.choice(start_pos))

    def bomb(self, heading, start_pos):
        missile = Missile(self.screen, heading, starting_pos=(start_pos, 400))
        missiles.append(missile)

    def move_missiles(self):
        for missile in missiles:
            if missile.xcor() < -220 or missile.xcor() > 220 or missile.ycor() < -160:
                missile.clear()
                missiles.remove(missile)
                del missile
            else:
                missile.forward(self.missile_speed)