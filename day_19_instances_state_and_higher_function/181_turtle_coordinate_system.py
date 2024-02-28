from turtle import Turtle, Screen
import random
screen = Screen()
tim  = Turtle()

screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x = -230, y = -100 + i*40)


    
screen.exitonclick()
