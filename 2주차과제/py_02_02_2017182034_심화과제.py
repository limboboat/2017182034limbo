import turtle
import random

def draw_circle():
    global c_x,c_y
    c_x,c_y=random.randint(0,300),random.randint(0,300)
    turtle.penup()
    turtle.goto(c_x,c_y)
    turtle.pendown()
    turtle.circle(50)
    turtle.penup()
    turtle.home()


def move_W():
        turtle.setheading(90)
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
        turtle.stamp()
        turtle.setheading(-90)
        restart()
        
def move_A():
        turtle.setheading(180)
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
        turtle.stamp()
        turtle.setheading(-180)
        restart()
        
def move_S():
        turtle.setheading(-90)
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
        turtle.stamp()
        turtle.setheading(90)
        restart()
        
def move_D():
        turtle.setheading(0)
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
        turtle.stamp()
        turtle.setheading(0)
        restart()
        
def restart():
    x,y=turtle.position()
    if ((x-c_x)**2+(y-c_y)**2)<=50**2:
        turtle.reset()
        turtle.home()
        draw_circle()
        turtle.pendown()


draw_circle()
turtle.pendown()
turtle.shape("turtle")

turtle.onkey(move_W,'W')
turtle.onkey(move_A,'A')
turtle.onkey(move_S,'S')
turtle.onkey(move_D,'D')
turtle.listen()
