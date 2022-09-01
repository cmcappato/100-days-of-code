import random
import turtle
import turtle as t
from random import randint

tim = t.Turtle()
""" Draw a square
for _ in range(4):
    tim.fd(100)
    tim.right(90)
"""
""" Draw a dashed line
for _ in range(15):
    tim.fd(10)
    tim.penup()
    tim.fd(10)
    tim.pendown()
"""
""" Draw from triangle to decagon
tim.hideturtle()
tim.penup()
tim.goto(-50, 200)
tim.showturtle()
tim.pendown()

is_decagon = False
number_of_sides = 3


while not is_decagon:
    internal_angle = 360 / number_of_sides
    tim.color(randint(0, 255), randint(0, 255), randint(0, 255))

    for side in range(number_of_sides):
        tim.forward(100)
        tim.right(internal_angle)
    number_of_sides += 1

    if number_of_sides == 10:
        is_decagon = True
"""
""" Draw a random walk with colours
def random_walk():
    t.colormode(255)
    directions = [0, 90, 180, 270]
    tim.hideturtle()
    tim.speed(15)
    tim.width(10)

    for _ in range(100):
        tim.fd(20)
        tim.setheading(random.choice(directions))
        tim.color(randint(0, 255), randint(0, 255), randint(0, 255))


random_walk()
"""


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)

    return rand_color


t.colormode(255)
angle = 0
tim.speed("fastest")

for _ in range(36):
    tim.setheading(angle)
    tim.circle(100)
    tim.color(random_color())
    angle += 10


screen = t.Screen()
screen.exitonclick()
