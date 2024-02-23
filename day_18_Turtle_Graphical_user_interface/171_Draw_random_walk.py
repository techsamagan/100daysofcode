from turtle import Turtle, Screen
import random

screen = Screen()

tim = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(10)

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.left(random.choice(directions))

screen.exitonclick()