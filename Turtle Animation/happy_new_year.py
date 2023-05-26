import turtle
from random import randint,choice
width=700
height =500
s=turtle.Screen()
s.setup(width,height)
s.bgcolor('black')
s.title("Fireworks")

colors=['red','green','yellow','gold','pink','cyan','white','orange','violet','coral']

class Fireworks:
    def __init__(self,radius):
        self.t=turtle.Pen()
        self.t.speed(0)
        self.t.color(choice(colors))
        self.t.hideturtle()
        self.t.up()
        self.t.down()
        self.radius=radius

    def update(self):
        self.t.forward(self.radius)
        self.t.backward(self.radius)
        self.t.left(10)
        

    def clean(self):
        self.t.clear()
        self.t.color(choice(colors))
        self.t.up()
        self.t.setposition(randint(-250,250),randint(0,200))
        self.t.down()


t1=Fireworks(randint(10,100))
t2=Fireworks(randint(10,100))
t3=Fireworks(randint(10,100))
t4=Fireworks(randint(10,100))
t5=Fireworks(randint(10,100))


t=turtle.Pen()
t.sety(-150)
t.color('gold')
t.write('Happy New Year 2023',align='center',font=(None,50))

while True:
    for i in range(36):
        t1.update()
        t2.update()
        t3.update()
        t4.update()
        t5.update()

    t1.clean()
    t2.clean()
    t3.clean()
    t4.clean()
    t5.clean()
turtle.mainloop()



