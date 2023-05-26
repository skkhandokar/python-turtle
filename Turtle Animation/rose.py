import turtle

#set initial position

turtle.penup()
turtle.goto(0,200)
turtle.pendown()

#rose flower base
turtle.fillcolor('#FF007F')
turtle.begin_fill()
turtle.circle(10,180)
turtle.circle(25,110)
turtle.left(50)
turtle.circle(60,45)
turtle.circle(20,170)
turtle.right(24)
turtle.forward(30)
turtle.left(10)
turtle.circle(30,110)
turtle.forward(20)
turtle.left(40)
turtle.circle(90,70)
turtle.circle(30,150)
turtle.right(30)
turtle.forward(15)
turtle.circle(80,90)
turtle.left(15)
turtle.forward(45)
turtle.right(165)
turtle.forward(20)
turtle.left(155)
turtle.circle(150,80)
turtle.left(50)
turtle.circle(150,90)
turtle.end_fill()
turtle.left(150)
turtle.circle(-90,70)
turtle.left(20)
turtle.circle(75,105)
turtle.setheading(60)
turtle.circle(80,98)
turtle.circle(-90,40)
turtle.left(180)
turtle.circle(90,40)
turtle.circle(-80,98)
turtle.setheading(-83)

#leaves1
turtle.forward(30)
turtle.left(90)
turtle.forward(25)
turtle.left(45)
turtle.fillcolor('green')
turtle.begin_fill()
turtle.circle(-80,90)
turtle.right(90)
turtle.circle(-80,90)
turtle.end_fill()
turtle.right(135)
turtle.forward(60)
turtle.left(180)
turtle.forward(85)
turtle.left(90)
turtle.forward(80)

#leaves2
turtle.right(90)
turtle.right(45)
turtle.fillcolor('green')
turtle.begin_fill()
turtle.circle(80,90)
turtle.left(90)
turtle.circle(80,90)
turtle.end_fill()
turtle.left(135)
turtle.forward(60)
turtle.left(180)
turtle.forward(60)
turtle.right(90)
turtle.circle(200,60)

def mov(x, y):
    tech_habit.up()
    tech_habit.setposition(0, 0)
    tech_habit.setheading(90)
    tech_habit.lt(90)
    tech_habit.fd(x)
    tech_habit.rt(90)
    tech_habit.fd(y)
    tech_habit.pendown()


tech_habit = turtle.Turtle()
mov(-75, 205)

tech_habit.pencolor("#95ed28")
style = ('Arial', 45, 'bold')
tech_habit.write("SORRY", font=style)
turtle.done()