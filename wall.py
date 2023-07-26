from turtle import Turtle



class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=100, stretch_len=1/4)
