import turtle
import pandas
from scoreboard import Textboard
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)


screen = turtle.Screen()
screen.setup(width=876, height=770)
screen.title('U.S. States Game')
image = "blank_nigeria_states.gif"
screen.addshape(image)
turtle.shape(image)
title_text = "Guess the State"
score = 0
guess_states = []
not_guessed_states = []
# is_game_on = True
while len(guess_states) < 37:
    answer_state = screen.textinput(title=title_text, prompt="What's another state's name? or type 'exit' to exit").title()
    data = pandas.read_csv("states_and_cord.csv")
    states = data.state
    if answer_state in guess_states:
        title_text = "Already Guessed."
    elif answer_state in states.values and answer_state not in guess_states:
        x_state = float(data[states == answer_state].x)
        y_state = float(data[states == answer_state].y)
        Textboard(answer_state, x_state, y_state)
        guess_states.append(answer_state)
        score += 1
        title_text = f"{score}/{len(states)} States Correct."
    elif answer_state == "Exit":
        for item in states:
            if item not in guess_states:
                not_guessed_states.append(item)
                df = pandas.DataFrame(not_guessed_states)
                df.to_csv("states_to_learn.csv", index=False)
        break
    else:
        title_text = "State not found."

