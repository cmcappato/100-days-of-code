import turtle
import pandas as pd

IMAGE = "blank_states_img.gif"
data = pd.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S. States Game")

screen.addshape(IMAGE)
turtle.shape(IMAGE)
all_states = data.state.tolist()
print(all_states)

states_guessed = []

while len(states_guessed) < 50:

    answer_state = (screen.textinput(title=f"{len(states_guessed)}/50 States Correct", prompt="What's the name of the state?")).title()
    if answer_state in all_states:
        states_guessed.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

    elif answer_state == 'Exit':
        missing = [state for state in all_states if state not in states_guessed]
        missing_states = pd.DataFrame(missing)
        missing_states.to_csv("states_to_learn.csv")
        break

