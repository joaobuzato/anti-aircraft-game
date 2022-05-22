from turtle import Turtle
from shot import Shot
STARTING_POS = (2, -70)
TURN_DEGREES = 45
cannon_img = "img/cannon.gif"
cannon_img_left_45 = "img/cannon-45.gif"
cannon_img_right_45 = "img/cannon45.gif"


class Cannon(Turtle):

    def __init__(self, screen):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.screen = screen
        self.goto(STARTING_POS)

        self.screen.register_shape(cannon_img)
        self.screen.register_shape(cannon_img_left_45)
        self.screen.register_shape(cannon_img_right_45)

        self.shape(cannon_img)

    def turn_right(self):
        if self.heading() < 135:
            self.setheading(self.heading()+TURN_DEGREES)
            if self.heading() == 90:
                self.shape(cannon_img)
            else:
                self.shape(cannon_img_right_45)

    def turn_left(self):
        if self.heading() > 45:
            self.setheading(self.heading()-TURN_DEGREES)
            if self.heading() == 90:
                self.shape(cannon_img)
            else:
                self.shape(cannon_img_left_45)

    def shoot(self):
        # TODO
        shot = Shot(self.screen, self.heading())
        return shot
