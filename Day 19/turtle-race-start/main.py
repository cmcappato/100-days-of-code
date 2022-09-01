from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
names = ["Donatello", "Leonardo", "Michelangelo", "Raphael", "Shelly", "Tim"]

starting_y_axis = -100


for turtle_index in range(6):
    tim = Turtle("turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=starting_y_axis)
    starting_y_axis += 40


screen.exitonclick()
