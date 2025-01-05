import random
from random import choice
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1

def increment_speed():
    global STARTING_MOVE_DISTANCE
    STARTING_MOVE_DISTANCE+=MOVE_INCREMENT

class CarManager(Turtle):
    def __init__(self,y):
        super().__init__()
        self.color(choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=0.5 , stretch_len=2)
        self.setheading(180)
        self.speed = 5
        self.penup()
        self.goto(300,y)

    def move(self):
        if self.xcor()>-300:
            self.forward(STARTING_MOVE_DISTANCE)
            return True
        else:
            return False

