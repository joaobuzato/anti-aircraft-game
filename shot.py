from turtle import Turtle
STARTING_POS = (0, -135)

SHOT_IMG = 'img/shot.gif'
SHOT_IMG_RIGHT = 'img/shot-right.gif'
SHOT_IMG_LEFT = 'img/shot-left.gif'


class Shot(Turtle):

    def __init__(self, screen, heading):
        super().__init__()
        self.screen = screen
        self.setheading(heading)
        self.penup()
        self.goto(STARTING_POS)
        self.screen.register_shape(SHOT_IMG)
        self.screen.register_shape(SHOT_IMG_RIGHT)
        self.screen.register_shape(SHOT_IMG_LEFT)
        if self.heading() == 90:
            self.shape(SHOT_IMG)
        elif self.heading() == 45:
            self.shape(SHOT_IMG_RIGHT)
        elif self.heading() == 135:
            self.shape(SHOT_IMG_LEFT)



