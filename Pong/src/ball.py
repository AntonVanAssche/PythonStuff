#!/usr/bin/env python3

from turtle import Turtle
from playsound import playsound
from threading import Thread
import os

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 2.5
        self.y_move = 2.5

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_y(self, path_to_sound=None):
        self.play_sound(path_to_sound)
        self.y_move *= -1

    def bounce_x(self, path_to_sound=None):
        self.play_sound(path_to_sound)
        self.x_move *= -1

    def bounce_wall(self):
        self.goto(0, 0)
        self.bounce_x()

    def locate_sound(self):
        self.dirs = ['/home/', 'c:\\']
        for dir in self.dirs:
            for r,d,f in os.walk(dir):
                for files in f:
                    if files == "pong.mp3":
                        return os.path.join(r, files)

    def play_sound(self, path_to_sound):
        play_thread = Thread(target = lambda: playsound(path_to_sound))
        play_thread.start()
