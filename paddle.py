from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()

        self.shape("square")
        self.color("white")

        self.shapesize(stretch_wid=5, stretch_len=1)

        self.penup()

        self.goto(x, y)


    def r_up(self):
        self.goto(360, self.ycor() + 50)

    def r_down(self):
        self.goto(360, self.ycor() - 50)

    def l_up(self):
        self.goto(-360, self.ycor() + 50)

    def l_down(self):
        self.goto(-360, self.ycor() - 50)




