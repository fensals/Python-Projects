from turtle import Turtle
import random


class Food(Turtle):  # making the food class inherit all attributes and methods of the turtle class

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        self.food_refresh()

    def food_refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
