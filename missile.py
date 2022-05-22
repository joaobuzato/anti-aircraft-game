from turtle import Turtle
import random

MISSILE_IMG = 'img/missile.gif'


class Missile(Turtle):

    def __init__(self, screen, heading, starting_pos):
        super().__init__()
        self.screen = screen
        self.setheading(heading)
        self.penup()
        self.goto(starting_pos)
        self.pencolor('red')
        self.pendown()
        self.screen.register_shape(MISSILE_IMG)
        if self.heading() == 270:
            self.shape(MISSILE_IMG)
        elif self.heading() == 45:
            self.shape(MISSILE_IMG)
        elif self.heading() == 135:
            self.shape(MISSILE_IMG)

