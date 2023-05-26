import turtle
import time

t=turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
x=0
y=0
t.pencolor('white')
t.home()
# t.write((x,y))
# t.speed(0)
y=-100
t.penup()
t.goto(x,y)
t.pendown()
t.begin_fill()
t.fillcolor("green")
t.circle(100)

t.penup()
t.end_fill()
t.home()
y=-60
t.goto(x,y)
t.pendown()
t.begin_fill()
t.fillcolor("red")
t.circle(60)
t.end_fill()
t.penup()

t.home()
t.left(90)
t.pencolor('yellow')
# t.goto(0,0)
for i in range(12):
    t.right(360/12)
    t.forward(85)
    t.write((i+1))
    t.goto(0,0)

def draw_hour_arm():
    t.penup()
    t.home()
    t.right(180)
    t.pendown()
    t.pensize(5)
    t.forward(40)


def draw_min_arm():
    t.penup()
    t.home()
    t.right(270)
    t.pendown()
    t.pensize(2)
    t.forward(70)

draw_hour_arm()
draw_min_arm()

angele=0
while True:
    sstart=time.time()
    start=1
    if start==1:
       t.penup()
       t.home()
       t.left(90)
       start=2
    t.right(angele)
    t.pendown()
    t.forward(60)
    time.sleep(1-(time.time()-sstart))
    t.undo()
    t.penup()
    t.goto(0,0)
    angele+=360/60

turtle.done()