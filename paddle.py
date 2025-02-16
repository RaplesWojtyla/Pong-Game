from turtle import Turtle

MOVE_DISTANCE = 25


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.pu()
        self.setpos(position)

    def go_up(self):
        if self.ycor() < 245:
            new_y = self.ycor() + MOVE_DISTANCE
            self.setpos(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - MOVE_DISTANCE
            self.setpos(self.xcor(), new_y)
