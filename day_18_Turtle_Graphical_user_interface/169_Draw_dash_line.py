from turtle import Turtle, Screen


sam = Turtle()
screen = Screen()

for _ in range(15):
    sam.forward(10)
    sam.penup()
    sam.forward(10)
    sam.pendown()
screen.exitonclick()