from turtle import Turtle
import pandas

data = pandas.read_csv("states_and_cord.csv")
states = len(data["state"])
ALIGNMENT = 'center'
FONT = 'Arial', 8, 'normal'


class Textboard(Turtle):
    def __init__(self, user_answer, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x_cor, y_cor)
        self.write(f"{user_answer}", align=ALIGNMENT, font=FONT)
