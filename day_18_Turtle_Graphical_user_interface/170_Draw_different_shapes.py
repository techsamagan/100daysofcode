from turtle import Turtle, Screen

tim = Turtle()
number = 3


while number < 15:
    angle = 180 - 360/number
    for _ in range(number):
        tim.forward(100)
        tim.left(angle)
    number += 1