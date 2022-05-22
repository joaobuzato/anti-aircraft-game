from turtle import Turtle
import random

MISSILE_IMG = 'img/missile.gif'
MISSILE_IMG_RIGHT15 = 'img/missile-right15.gif'
MISSILE_IMG_RIGHT30 = 'img/missile-right30.gif'
MISSILE_IMG_RIGHT45 = 'img/missile-right45.gif'
MISSILE_IMG_RIGHT60 = 'img/missile-right60.gif'
MISSILE_IMG_LEFT15 = 'img/missile-left15.gif'
MISSILE_IMG_LEFT30 = 'img/missile-left30.gif'
MISSILE_IMG_LEFT45 = 'img/missile-left45.gif'
MISSILE_IMG_LEFT60 = 'img/missile-left60.gif'

angles_dict = {
    330: MISSILE_IMG_RIGHT60,
    315: MISSILE_IMG_RIGHT45,
    300: MISSILE_IMG_RIGHT30,
    285: MISSILE_IMG_RIGHT15,
    270: MISSILE_IMG,
    255: MISSILE_IMG_LEFT15,
    240: MISSILE_IMG_LEFT30,
    225: MISSILE_IMG_LEFT45,
    210: MISSILE_IMG_LEFT60
}



class Missile(Turtle):

    def __init__(self, screen, heading, starting_pos):
        super().__init__()
        self.screen = screen
        self.setheading(heading)
        self.penup()
        self.goto(starting_pos)
        self.pencolor('red')
        self.pendown()
        for key, value in angles_dict.items():
            self.screen.register_shape(value)

        self.shape_manager()

    def shape_manager(self):
        self.shape(angles_dict.get(int(self.heading())))


