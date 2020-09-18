import turtle

def move_W():
        turtle.setheading(90)
        turtle.forward(50)
        turtle.stamp()
        turtle.setheading(-90)
        
def move_A():
        turtle.setheading(180)
        turtle.forward(50)
        turtle.stamp()
        turtle.setheading(-180)
        
def move_S():
        turtle.setheading(-90)
        turtle.forward(50)
        turtle.stamp()
        turtle.setheading(90)
        
def move_D():
        turtle.setheading(0)
        turtle.forward(50)
        turtle.stamp()
        turtle.setheading(0)
        
def move_ESC():        
    turtle.reset()
        

turtle.shape("turtle")
turtle.onkey(move_W,'W')
turtle.onkey(move_A,'A')
turtle.onkey(move_S,'S')
turtle.onkey(move_D,'D')
turtle.onkey(move_ESC,'Escape')
turtle.listen()
