from turtle import Turtle
STARTING_POS = (2, -70)

SHOT_IMG = 'img/shot.gif'


class Shot(Turtle):

    def __init__(self, screen, heading):
        super().__init__()
        self.screen = screen
        self.setheading(heading)
        self.penup()
        self.goto(STARTING_POS)
        self.screen.register_shape(SHOT_IMG)
        self.shape(SHOT_IMG)

    def move(self):
        self.forward(10)



