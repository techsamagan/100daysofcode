from turtle import Turtle, Screen

tim = Turtle()
screen  = Screen()

def move_forward():
    tim.penup()
    tim.forward(10)
def drive():
    tim.forward(10)
def reverse():
    tim.backward(10)
def right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clean():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    

screen.listen()
screen.onkey(key ="space", fun = move_forward)
screen.onkey(key = "w", fun = drive)
screen.onkey(key = "s", fun = reverse)
screen.onkey(key = "a", fun = left)
screen.onkey(key = "d", fun = right)
screen.onkey(key = "c", fun = clean)
screen.exitonclick()