import turtle
from turtle import Turtle

STARTING = ((0, 0), (-20, 0), (-40, 0))
MOVE_DIST = 20  # distance for every move request
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []  # empty list to contain the 3 segments of the snake
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.pu()
        new_segment.goto(position)
        new_segment.color('white')
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # to help the snake segments move together irrespective of direction
            # as first segment moves, 2nd takes position of 1st, 3rd takes the old position of 2nd
            # picking the old co-ordinates of a segment and assigning it as new cord. for the succeeding segment

            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
