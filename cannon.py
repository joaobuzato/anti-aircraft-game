from turtle import Turtle
STARTING_POS = (2, -70)
TURN_DEGREES = 45


class Cannon(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POS)

    def turn_right(self):
        if self.heading() < 135:
            self.setheading(self.heading()+TURN_DEGREES)

    def turn_left(self):
        if self.heading() > 45:
            self.setheading(self.heading()-TURN_DEGREES)

    def shoot(self):
        # TODO
        print("shoot")
        pass
