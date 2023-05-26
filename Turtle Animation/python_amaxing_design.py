from turtle import *
from time import sleep

bgcolor("black")
t = [Turtle(), Turtle()]
x = 6
colors = ["red", "gold", "lime","silver"]
for index, j in enumerate(t):
	j.speed(0)
	j.color("white")
	j.shape("circle")
	j.shapesize(0.3)
	j.width(3)
	j.pu()
	j.seth(90)
	j.fd(350)
	j.seth(-180)
	j.pd()
t[0].pu()

delay(0)
speed(0)
ht()
sleep(1)
for i in colors:
	color(i)
	for i in range(360):
		t[0].fd(x)
		t[0].lt(1)
		pu()
		goto(t[0].pos())
		pd()
		t[1].fd(2 * x)
		t[1].lt(2)
		goto(t[1].pos())
done()