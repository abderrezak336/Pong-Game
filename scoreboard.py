from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.updatescreen()

    def updatescreen(self):
        self.clear()

        self.goto(30, 260)
        self.write(self.r_score, align="center", font=("arial", 30, "normal"))
        self.goto(-30, 260)
        self.write(self.l_score, align="center", font=("arial", 30, "normal"))




    def increas_l_score(self):
        self.l_score += 1
        self.updatescreen()

    def increas_r_score(self):
        self.r_score += 1
        self.updatescreen()



