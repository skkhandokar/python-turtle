import turtle as t
import random as r
from PIL import ImageTk
import tkinter as tk

t.speed(10)
def star():
    t.left(50)
    t.forward(50)
    t.pencolor("white")
    t.begin_fill()
    for _ in range(5):
        t.color("white")
        t.forward(51)
        t.left(144)
    t.end_fill()

t.pen(pensize=5,pencolor="white")
wn = t.Screen()

t.bgcolor("#000000")
t.up()
t.goto(-50,15)
t.down()
t.begin_fill()
t.color('white')
t.circle(120)
t.end_fill()

t.up()
t.goto(-20,25)
t.down()
t.begin_fill()
t.color('#000000')
t.circle(120)
t.end_fill()

star()

for _ in range(30):
    l=r.randint(5,12)
    x=r.randint(-610,650)
    y=r.randint(-350,350)
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    for _ in range(5):
        t.color('white')
        t.forward(1)
        t.left(144)
    t.end_fill()

def write(message,pos,color):
    x,y=pos
    t.color(color)
    t.penup()
    t.goto(x,y)
    t.pendown()
    style=('Courier',40,"bold")
    t.write(message,font=style)
t.up()
write("EID",(80,25),"white")
write("MUBARAK",(25,-25),"white")


t.done()