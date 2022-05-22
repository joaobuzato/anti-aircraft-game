from turtle import Turtle
STARTING_POS = (2, -70)
TURN_DEGREES = 45


class Cannon(Turtle):

    def __init__(self, screen):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.screen = screen
        self.goto(STARTING_POS)
        self.cannon_img = "img/cannon.gif"
        self.cannon_img_left_45 = "img/cannon-45.gif"
        self.cannon_img_right_45 = "img/cannon45.gif"

        self.screen.register_shape(self.cannon_img)
        self.screen.register_shape(self.cannon_img_left_45)
        self.screen.register_shape(self.cannon_img_right_45)

        self.shape(self.cannon_img)

    def turn_right(self):
        if self.heading() < 135:
            self.setheading(self.heading()+TURN_DEGREES)
            if self.heading() == 90:
                self.shape(self.cannon_img)
            else:
                self.shape(self.cannon_img_right_45)

    def turn_left(self):
        if self.heading() > 45:
            self.setheading(self.heading()-TURN_DEGREES)
            if self.heading() == 90:
                self.shape(self.cannon_img)
            else:
                self.shape(self.cannon_img_left_45)

    def shoot(self):
        # TODO
        print("shoot")
        pass
