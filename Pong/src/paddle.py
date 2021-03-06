#!/usr/bin/env python3

from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        if not self.ycor() >= 240:
            y = self.ycor() + 40
            self.goto(self.xcor(), y)

    def go_down(self):
        if not self.ycor() <= -240:
            y = self.ycor() - 40
            self.goto(self.xcor(), y)
