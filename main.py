import random
import turtle

import colorgram as c
from turtle import Turtle, Screen
from random import Random

# Формируем цветовую гамму точек при помощи Colorgram
color_items = c.extract("image_1.png", 15)
print(color_items)
colors = []

for item in color_items:
    colors.append((item.rgb.r, item.rgb.g, item.rgb.b))

# print(colors)

# colors = [(183, 73, 46), (161, 157, 23), (230, 219, 194), (19, 122, 150), (223, 210, 217), (45, 46, 99), (11, 20, 35), (234, 222, 98), (150, 162, 178), (104, 107, 174), (213, 221, 218), (169, 23, 46), (218, 143, 90), (190, 190, 198)]

tim = Turtle()
my_scr = Screen()
turtle.colormode(255)

my_scr.canvheight = 225
my_scr.canvwidth = 225
pendown = False
tim.pen(pendown=pendown)

for j in range(10):
    tim.goto(-my_scr.canvwidth, -my_scr.canvheight + j*50)
    for i in range(10):
        tim.pen(pencolor=random.choice(colors))
        print(f"Tim's столбец {i} строка {j} координата:{tim.pos()}")
        tim.dot(20)
        # tim.pen(pendown=not pendown)
        tim.forward(50)

print(tim.pos())
my_scr.exitonclick()