from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_anticlockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def move_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="f", fun = move_forward)
screen.onkey(key = "b", fun = move_backward)
screen.onkey(key = "l", fun = move_anticlockwise)
screen.onkey(key = "k", fun = move_clockwise)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()