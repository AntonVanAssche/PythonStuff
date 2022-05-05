#!/usr/bin/env python3

# Import libraries.
from turtle import Screen
from paddle import Paddle
from playsound import playsound
from ball import Ball
from score import Score
import time

# Create and build the window.
screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong written in Python!")

# Hide the paddles till they are on the correct side of the screen.
screen.tracer(0)

# Define both paddles.
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

# Define the ball
ball = Ball()

# Define the maximum distance from the center of the ball
# To the center of the paddle. This is needed for calculating
# when the ball hits a paddle.
max_distance = (20 ** 2 + 60 ** 2) ** (1/2)

# Define and set the scoreboard to `0 0`.
score = Score()

def main():
    screen.listen()

    # Right paddle navigation.
    # Using the arrow keys `↑` and `↓`.
    screen.onkey(right_paddle.go_up, "Up")
    screen.onkey(right_paddle.go_down, "Down")

    # Left Paddle navigation
    # `w` to go up and `s` to go down.
    screen.onkey(left_paddle.go_up, "w")
    screen.onkey(left_paddle.go_down, "s")

    # This is for Azerty users
    screen.onkey(left_paddle.go_up, "z")

    while True:
        time.sleep(0.01)
        screen.update()
        ball.move()

        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.bounce_y()
            playsound('./src/sound/pong.mp3', False)

        if ball.distance(right_paddle) < max_distance and ball.xcor() == 330:
            ball.bounce_x()
            playsound('./src/sound/pong.mp3', False)

        if ball.distance(left_paddle) < max_distance and ball.xcor() == -330:
            ball.bounce_x()
            playsound('./src/sound/pong.mp3', False)

        if ball.xcor() == 390:
            ball.bounce_wall()
            playsound('./src/sound/pong.mp3', False)
            score.left_add_point()

        if ball.xcor() == -390:
            ball.bounce_wall()
            playsound('./src/sound/pong.mp3', False)
            score.right_add_point()

try:
    main()
except Exception:
    pass
