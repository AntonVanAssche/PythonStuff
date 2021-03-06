#!/usr/bin/env python3

from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(200, 200)
        self.write(self.right_score, align="center" ,font=("Comic Sans", 50, "normal"))
        self.goto(-200, 200)
        self.write(self.left_score, align="center" ,font=("Comic Sans", 50, "normal"))

    def left_add_point(self):
        self.left_score += 1
        if self.left_score == 5:
            self.left_score = "Winner"
        self.update_score()

    def right_add_point(self):
        self.right_score += 1
        if self.right_score == 5:
            self.right_score = "Winner"
        self.update_score()
