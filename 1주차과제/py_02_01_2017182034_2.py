import turtle

count=0;

while(count<=500):
    turtle.penup()
    turtle.goto(-250,count-250)
    turtle.pendown()
    turtle.forward(500)
    count=count+100

turtle.left(90)

count=0

while(count<=500):
    turtle.penup()
    turtle.goto(count-250,-250)
    turtle.pendown()
    turtle.forward(500)
    count=count+100
