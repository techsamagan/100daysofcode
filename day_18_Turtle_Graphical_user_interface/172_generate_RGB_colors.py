import turtle as t
from turtle import Screen
import random

screen = Screen()

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(10)

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.left(random.choice(directions))

screen.exitonclick()