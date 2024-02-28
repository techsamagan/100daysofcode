from turtle import Turtle, Screen
import random
screen = Screen()
tim  = Turtle()

is_race_on = False
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for i in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x = -230, y = -100 + i*40)
    all_turtles.append(tim)

if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:
         if turtle.xcor() > 230:
             is_race_on = False
             winning_color = turtle.pencolor()
             if winning_color == user_bet:
                 print(f"You've won! The turtle with {winning_color} won!")
             else:
                 print(f"You've lose! The turtle with {winning_color} won!")
         random_distance = random.randint(0, 10)
         turtle.forward(random_distance)
         
    
screen.exitonclick()
