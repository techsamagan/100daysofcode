import turtle as turtle_module
import random
from turtle import Screen
turtle_module.colormode(255)

tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
screen = Screen()
tim.left(225)
tim.forward(320)
tim.left(135)
circle_count = 0 
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color
for i in range(100):
    tim.dot(20,random_color() )
    circle_count += 1
    tim.forward(50)
    if circle_count%10 == 0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.left(180)
screen.exitonclick()

