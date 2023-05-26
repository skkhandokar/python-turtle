# import turtle
# from time import sleep

# t = turtle.Turtle()
# t.speed(4)
# turtle.bgcolor("white")
# t.color("white")
# turtle.title('Netflix Logo')

# t.up()
# t.goto(-80, 50)
# t.down()
# t.fillcolor("black")
# t.begin_fill()

# t.forward(200)
# t.setheading(270)
# s = 360
# for i in range(9):
#     s = s - 10
#     t.setheading(s)
#     t.forward(10)

# t.forward(180)
# s = 270
# for i in range(9):
#     s = s - 10
#     t.setheading(s)
#     t.forward(10)

# t.forward(200)
# s = 180
# for i in range(9):
#     s = s - 10
#     t.setheading(s)
#     t.forward(10)

# t.forward(180)
# s = 90
# for i in range(9):
#     s = s - 10
#     t.setheading(s)
#     t.forward(10)
# t.forward(30)
# t.end_fill()

# t.up()
# t.color("black")
# t.setheading(270)
# t.forward(240)
# t.setheading(0)
# t.down()
# t.color("red")
# t.fillcolor("#E50914")
# t.begin_fill()
# t.forward(30)
# t.setheading(90)
# t.forward(180)
# t.setheading(180)
# t.forward(30)
# t.setheading(270)
# t.forward(180)
# t.end_fill()
# t.setheading(0)
# t.up()
# t.forward(75)
# t.down()
# t.color("red")
# t.fillcolor("#E50914")
# t.begin_fill()
# t.forward(30)
# t.setheading(90)
# t.forward(180)
# t.setheading(180)
# t.forward(30)
# t.setheading(270)
# t.forward(180)
# t.end_fill()
# t.color("red")
# t.fillcolor("red")
# t.begin_fill()
# t.setheading(113)
# t.forward(195)
# t.setheading(0)
# t.forward(31)
# t.setheading(293)
# t.forward(196)
# t.end_fill()
# t.hideturtle()

# sleep(10)

# turtle.done()
















from turtle import *
import turtle as t
t.title('Netflix Logo by SK Khandokar')
sc=t.Screen()
sc.setup(500,500)
bgcolor('black')
right(90)
pos=[(-40,0), (40,0)]
for x,y in pos:
    up()
    goto(x,y)
    down()
    fillcolor('red')
    begin_fill()
    for i in range(2):
        forward(200)
        left(90)
        forward(40)
        left(90)
    end_fill()
up()
goto(-40,0)
down()
left(22)
   
begin_fill()
for i in range(2):
    forward(217)
    left(68)
    forward(40)
    left(112)
t.goto(-65,10)
t.pendown()

t.pencolor('red')
style = ('ConcaveB', 30, 'italic')
t.write("NETFLIX", font=style)
end_fill()
t.done()