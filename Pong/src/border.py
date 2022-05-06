#!/usr/bin/env python3

from turtle import Turtle

class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-400, -300)
        self.pendown()
        self.goto(-400, -300)
        self.goto(400, -300)
        self.goto(400, 300)
        self.goto(-400, 300)
        self.goto(-400, -300)

