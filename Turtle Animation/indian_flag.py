import turtle
from turtle import*
import time 
#screen for output
screen = turtle.Screen()
time.sleep(1)
# Defining a turtle Instance
t = turtle.Turtle()
speed(0)

# initially penup()
t.penup()
t.goto(-400, 250)
t.pendown()

# Orange Rectangle
#white rectangle
t.color("orange")
t.begin_fill()
t.forward(800)
t.right(90)
t.forward(167)
t.right(90)
t.forward(800)
t.end_fill()
t.left(90)
t.forward(167)

# Green Rectangle
t.color("green")
t.begin_fill()
t.forward(167)
t.left(90)
t.forward(800)
t.left(90)
t.forward(167)
t.end_fill()

# Big Blue Circle
t.penup()
t.goto(70, 0)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(70)
t.end_fill()

# Big White Circle
t.penup()
t.goto(60, 0)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(60)
t.end_fill()

# Mini Blue Circles
t.penup()
t.goto(-57, -8)
t.pendown()
t.color("navy")
for i in range(24):
	t.begin_fill()
	t.circle(3)
	t.end_fill()
	t.penup()
	t.forward(15)
	t.right(15)
	t.pendown()
	
# Small Blue Circle
t.penup()
t.goto(20, 0)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()
# Spokes
t.penup()
t.goto(0, 0)
t.pendown()
t.pensize(2)
for i in range(24):
	t.forward(60)
	t.backward(60)
	t.left(15)
	
#to hold the
#output window
t.penup()
t.setposition(-119, 240)
t.pencolor("orange")
style = ('Arial', 70, 'bold')
t.write("I", font=style)

t.setposition(-95, 240)
t.pencolor("green")
t.write("N", font=style)

t.setposition(-35, 240)
t.pencolor("navy")
t.write("D", font=style)

t.setposition(29, 240)
t.pencolor("orange")
t.write("I", font=style)

t.setposition(54, 240)
t.pencolor("green")
t.write("A", font=style)

t.setposition(590, 280)
t.pencolor("green")
t.write("A", font=style)
t.penup()
turtle.done()
