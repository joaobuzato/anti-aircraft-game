from turtle import Turtle
from shot_manager import ShotManager
STARTING_POS = (2, -70)
TURN_DEGREES = 45
cannon_img = "img/cannon.gif"
cannon_img_left = "img/cannon-left.gif"
cannon_img_right = "img/cannon-right.gif"


class Cannon(Turtle):

    def __init__(self, screen):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.screen = screen
        self.goto(STARTING_POS)
        self.shot_manager = ShotManager()

        self.screen.register_shape(cannon_img)
        self.screen.register_shape(cannon_img_left)
        self.screen.register_shape(cannon_img_right)

        self.shape(cannon_img)

    def turn_right(self):
        if self.heading() > 45:
            self.setheading(self.heading()-TURN_DEGREES)
            if self.heading() == 90:
                self.shape(cannon_img)
            else:
                self.shape(cannon_img_right)

    def turn_left(self):
        if self.heading() < 135:
            self.setheading(self.heading() + TURN_DEGREES)
            if self.heading() == 90:
                self.shape(cannon_img)
            else:
                self.shape(cannon_img_left)

    def shoot(self):
        self.shot_manager.shoot(self.screen, self.heading)
        pass

    def move_shots(self):
        self.shot_manager.move_shots()
