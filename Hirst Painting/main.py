from turtle import Turtle, Screen
import turtle
import random
#import colorgram

# import hirst

# extracting colors from an image using cologram and putting the result into
# a list containing tuples of r-g-b figures
# colors = colorgram.extract('hirst.jpg', 30)
# my_color = []
# # for i in colors:
# #     color = i.rgb
# #     r = color.r
# #     g = color.g
# #     b = color.b
# #     new_color = (r, g, b)
# #     my_color.append(new_color)

jum = Turtle()

jum.speed(0)

color_list = [(196, 169, 98), (242, 246, 250), (130, 177, 191), (160, 57, 77), (231, 219, 123), (51, 112, 163),
              (110, 91, 85), (138, 184, 127), (212, 152, 170), (67, 124, 76), (93, 124, 179), (86, 163, 95),
              (195, 69, 90), (150, 32, 47), (64, 53, 49), (204, 118, 46), (221, 170, 182), (151, 118, 108),
              (74, 59, 57), (157, 203, 217), (176, 205, 181), (222, 178, 169), (94, 139, 157), (86, 30, 37),
              (172, 189, 216), (33, 68, 96)]
turtle.colormode(255)

jum.hideturtle()


def color():
    """selects a random color from color list"""
    my_color = random.choice(color_list)
    return my_color


a = -240
b = -240
jum.pu()
for j in range(10):
    jum.goto(a, b)
    for i in range(10):
        jum.dot(20, color())
        jum.forward(50)

    b += 50

screen = Screen()
screen.exitonclick()
