import turtle as tr
import colorsys
import time
tr.bgcolor('black')
tr.tracer(10)
tr.width(55)
time.sleep(2)
h=0
for n in range(440):
    tr.speed(1)
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=0.005
    tr.color(c)
    tr.up()
    tr.goto(0,0)
    tr.fd(n)
    tr.down()
    tr.circle(n,4)
    tr.lt(85)

tr.done()
