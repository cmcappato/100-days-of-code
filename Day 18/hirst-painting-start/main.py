# This code will not work in repl.it as there is no access to the colorgram package here
# We talk about this in the video tutorial
"""
import colorgram

rgb_colors = []
colors = colorgram.extract('spot-painting.jpg', 50)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
"""
import turtle as t
import random

tim = t.Turtle()

color_list = [(39, 99, 181), (93, 172, 214), (172, 50, 85), (79, 107, 208), (220, 63, 103), (171, 26, 15),
              (219, 127, 167), (74, 174, 84), (228, 72, 47), (60, 119, 64), (123, 224, 184), (19, 54, 151),
              (236, 161, 207), (139, 214, 231), (41, 171, 186), (164, 169, 232), (30, 38, 82), (248, 9, 19),
              (37, 83, 47), (73, 77, 40)]
rows = 10
columns = 10

t.colormode(255)
y = -250


def change_start_position():
    tim.hideturtle()
    tim.penup()
    tim.goto(-250, y)


def move_turtle(y_axis):
    tim.hideturtle()
    tim.penup()
    tim.goto(-250, y_axis)


def draw_dots():
    tim.dot(20, random.choice(color_list))
    tim.hideturtle()
    tim.penup()
    tim.forward(50)


change_start_position()
tim.speed("fastest")

while not rows == 0:
    for _ in range(columns):
        draw_dots()
    y += 50
    move_turtle(y)
    rows -= 1

screen = t.Screen()
screen.exitonclick()

print(len(color_list))
