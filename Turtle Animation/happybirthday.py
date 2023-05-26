import turtle
import time


ankita = turtle.Screen()
ankita.bgcolor("black")
tech_habit = turtle.Turtle()
tech_habit.width(7)
colors = ["#f5ac2f", "#279cf5", "#d820f5", "#a2f52f", "#f527c1"]
time.sleep(5)

def draw_ankita(i, x, y):
    tech_habit.pencolor("linen")
    tech_habit.color(colors[i % 7])
    tech_habit.lt(70)
    tech_habit.penup()
    tech_habit.goto(x, y)
    tech_habit.pendown()
    tech_habit.circle(22)
    tech_habit.end_fill()


def ballon(x, y):
    tech_habit.pensize(4)
    for i in range(5):
        draw_ankita(i, x, y)


def f1():
    for i in range(7):
        tech_habit.pensize(5)
        tech_habit.pencolor('light blue')
        tech_habit.color(colors[i % 19])
        tech_habit.begin_fill()
        tech_habit.left(330)
        tech_habit.forward(55)
        tech_habit.begin_fill()
        tech_habit.rt(110)
        tech_habit.circle(33)
        tech_habit.end_fill()
        tech_habit.rt(11)
        tech_habit.backward(33)
        tech_habit.end_fill()


def cake(x, y):
    tech_habit.fd(x)
    tech_habit.rt(90)
    tech_habit.fd(y)
    tech_habit.rt(90)
    tech_habit.fd(x)
    tech_habit.rt(90)
    tech_habit.fd(y)


def move(x, y):
    tech_habit.up()
    tech_habit.setposition(0, 0)
    tech_habit.setheading(90)
    tech_habit.rt(90)
    tech_habit.fd(x)
    tech_habit.lt(90)
    tech_habit.fd(y)
    tech_habit.pendown()


def mov(x, y):
    tech_habit.up()
    tech_habit.setposition(0, 0)
    tech_habit.setheading(90)
    tech_habit.lt(90)
    tech_habit.fd(x)
    tech_habit.rt(90)
    tech_habit.fd(y)
    tech_habit.pendown()


def A(size):
    tech_habit.rt(19)
    tech_habit.forward(size)
    tech_habit.rt(141)
    tech_habit.fd(size)
    tech_habit.backward(size / 2)
    tech_habit.rt(105)
    tech_habit.fd(int(size / 3))


def B(size):
    tech_habit.forward(size)
    tech_habit.rt(90)
    for i in range(18):
        tech_habit.rt(9)
        tech_habit.fd(size // 20)
    for i in range(18):
        tech_habit.rt(size // 5)
        tech_habit.backward(size // 20)


def D(size):
    tech_habit.fd(size)
    tech_habit.rt(90)
    tech_habit.fd(size // 10)
    for i in range(13):
        tech_habit.rt(13)
        tech_habit.fd(size // 8)


def E(size):
    tech_habit.rt(90)
    tech_habit.fd(int(size / 3))
    tech_habit.back(int(size / 3))
    tech_habit.left(90)
    tech_habit.fd(size / 2)
    tech_habit.rt(90)
    tech_habit.fd(int(size / 3))
    tech_habit.back(int(size / 3))
    tech_habit.lt(90)
    tech_habit.fd(size / 2)
    tech_habit.rt(90)
    tech_habit.fd(int(size / 3))

def F(size):   
    tech_habit.fd(int(size / 2))  
    tech_habit.rt(90)
    tech_habit.fd(int(size / 2))
    tech_habit.lt(-90)
    tech_habit.rt(90)
    tech_habit.fd(int(size / 2))
    tech_habit.rt(90)
    tech_habit.fd(int(size / 2))
    tech_habit.rt(90)
    tech_habit.fd(int(size / 2))

    

def G(size):
        tech_habit.pensize(10)
        tech_habit.penup()
        tech_habit.fd(size // 2)
        tech_habit.pendown()
        tech_habit.lt(90)
        tech_habit.fd(size // 4)
        tech_habit.backward(size // 1.5)
        tech_habit.lt(90)
        for _ in range(size):
            tech_habit.rt(4)
            tech_habit.fd(4)


def H(size):
    tech_habit.fd(size)
    tech_habit.backward(size // 2)
    tech_habit.rt(90)
    tech_habit.fd(size // 2)
    tech_habit.lt(90)
    tech_habit.fd(size // 2)
    tech_habit.backward(size)


def I(size):
    tech_habit.fd(size)
    tech_habit.rt(90)
    tech_habit.circle(size // 8)

def J(size):
    tech_habit.fd(size)
    tech_habit.lt(90)
    tech_habit.fd(int(size/2)) 
    tech_habit.back(int(size/2))
    tech_habit.rt(90)
    tech_habit.back(int(size/1))
    tech_habit.lt(110)
    tech_habit.fd(int(size/5)) 
    tech_habit.rt(30)   
    tech_habit.fd(int(size/7))

def K (size):
    tech_habit.fd(int(size / 1))
    tech_habit.back(int(size/2))
    tech_habit.rt(135)
    tech_habit.fd( int(size / 1.5))  
    tech_habit.back(int(size/1.5))
    tech_habit.rt(270)
    tech_habit.fd( int(size / 1.5))

def L(size):
    tech_habit.rt(90)
    tech_habit.fd(int(size / 2))
    tech_habit.back(int(size / 2))
    tech_habit.lt(90)
    tech_habit.fd(size)

def N(size):
    tech_habit.fd(size)
    tech_habit.rt(150)
    tech_habit.fd(size + int(size / 6))
    tech_habit.lt(150)
    tech_habit.fd(size)


def M(size):
    tech_habit.fd(size)
    tech_habit.rt(150)

    tech_habit.fd( size /2)
    tech_habit.lt(120)

    tech_habit.fd(size/2)
    tech_habit.rt(147)
    tech_habit.fd(size )

def P(size):
    tech_habit.fd(size)
    tech_habit.rt(90)
    tech_habit.fd(size // 8)
    for i in range(8):
        tech_habit.rt(20)
        tech_habit.fd(size // 9)

def R():
    tech_habit.fd(60)
    tech_habit.rt(90)
    tech_habit.fd(7)
    for i in range(15):
        tech_habit.rt(12)
        tech_habit.fd(3)
    tech_habit.lt(120)
    tech_habit.fd(40)


def S(size):
    tech_habit.rt(90)
    for i in range(0, 5):
        if i < 3:
            tech_habit.fd(size / 2)
            tech_habit.lt(90)
            if i == 2:
                tech_habit.rt(90)
        else:
            tech_habit.right(90)
            tech_habit.fd(size / 2)


def T(size):
    tech_habit.fd(size)
    tech_habit.rt(90)
    tech_habit.fd(size // 2)
    tech_habit.backward(size // 2)



def U(size):
    tech_habit.rt(90)
    for i in range(size // 10):
        tech_habit.lt(15)
        tech_habit.fd(size // 10)
    tech_habit.fd(size // 2)
    tech_habit.back(size // 2)

    for i in range(size // 10):
        tech_habit.rt(13)
        tech_habit.back(size // 10)
    tech_habit.lt(5)
    for i in range(size // 10):
        tech_habit.rt(17)
        tech_habit.back(size // 10)
    tech_habit.back(size // 2)


def Y(size):
    tech_habit.fd(size)
    tech_habit.left(60)
    tech_habit.fd(size // 2)
    tech_habit.backward(size // 2)
    tech_habit.rt(90)
    tech_habit.fd(size // 1.5)

tech_habit.speed(19)

#ABDEFGHIJLMNPRSTY

mov(120, 30)
tech_habit.color("#f7b543")
# tech_habit.color(colors[8 % 5])
tech_habit.begin_fill()
cake(40, 180)
tech_habit.end_fill()
mov(110, 75)
tech_habit.color("#d152f7")
tech_habit.begin_fill()
cake(40, 160)
tech_habit.end_fill()
mov(100, 120)
tech_habit.color("#f54eb8")
tech_habit.begin_fill()
cake(40, 140)
tech_habit.end_fill()
mov(30, 170)
tech_habit.width(11)
tech_habit.pencolor("red")
tech_habit.circle(7)
move(180, 307)
mov(0, 0)
ballon(-490, 200)
ballon(490, 200)
ballon(183, -150)
ballon(-133, -150)

tech_habit.speed(7)
tech_habit.width(9)
tech_habit.pencolor('red')
mov(260, 205)
M(size=80)

tech_habit.width(11)
#NAME HERE NILESH HAPPY BIRTHDAY190
mov(198, 205)
B(80)
mov(169, 205)
A(size=80)
mov(105, 205)
P(size=80)
mov(70, 205)
P(size=80)
mov(29, 205)
E(size=80)
mov(-11, 205)
tech_habit.pencolor("green")
style = ('Arial', 40, 'italic')
tech_habit.write("(Ligend)", font=style)

tech_habit.pencolor("cyan")
tech_habit.width(13)
mov(260, -80)
H(100)
tech_habit.width(7)
mov(190, -80)
A(65)
mov(135, -80)
P(60)
mov(100, -80)
P(60)
mov(52, -80)
Y(60)
mov(28, -80)
B(60)
move(12, -80)
I(60)
move(36, -80)
R()
move(80, -80)
T(100)
move(102, -80)
H(60)
move(150, -80)
tech_habit.pencolor('hotpink')
D(200)
move(160, -80)
A(60)
move(220, -80)
Y(60)

# tech_habit.width(5)
# move(-138, -270)
# tech_habit.pencolor("green")
# style = ('Arial', 8, 'bold')
# tech_habit.write("Department Of Economic ", font=style)
# move(2, -270)
# tech_habit.pencolor("red")
# tech_habit.write("2018-19 Master's Batch ", font=style)

# move(130, -270)
# tech_habit.pencolor("white")
# tech_habit.write("Of MC College", font=style)
time.sleep(5)
# ankita.exitonclick()