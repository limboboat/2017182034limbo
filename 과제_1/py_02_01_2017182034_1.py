import turtle

def draw_Wline(a,b):
    turtle.penup()
    turtle.goto(a,b)
    turtle.pendown()
    turtle.forward(300)

def draw_Hline(a,b):
    turtle.penup()
    turtle.goto(a,b)
    turtle.pendown()
    turtle.forward(250)

def draw_line(a,b,c):
    turtle.penup()
    turtle.goto(a,b)
    turtle.pendown()
    turtle.forward(c)

draw_Wline(-550,0)
draw_Wline(-550,-250)

draw_Wline(-150,125)
draw_Wline(-150,0)
draw_Wline(-150,-250)

draw_Wline(250,125)
draw_Wline(250,0)
draw_line(600,0,100)

turtle.right(90)

draw_Hline(-250,250)
draw_Hline(-550,0)
draw_Hline(-250,0)

draw_Hline(-150,250)
draw_Hline(150,250)
draw_Hline(0,0)

draw_Hline(250,250)
draw_Hline(550,250)
draw_line(600,250,500)
draw_line(700,250,500)

turtle.right(90)
turtle.penup()
turtle.goto(-500,225)
turtle.pendown()
turtle.circle(100)

turtle.exitonclick()
