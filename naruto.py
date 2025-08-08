import turtle 

screen = turtle.Screen()
screen.setup(900,900)
screen.setworldcoordinates(-600,-600,600,500)

d = turtle.Turtle()

d.pencolor("red")
d.pensize(4)
d.hideturtle()

turtle.tracer(1)
d.pencolor('black')
d.left(13)

d.speed(1)
d.fillcolor("yellow")
d.begin_fill()
d.penup()
d.forward(190)
d.pendown()

d.right(25)
d.forward(60)
d.left(135)
d.forward(100)
d.right(95)
d.forward(95)
d.left(135)
d.forward(110)
d.right(105)
d.forward(115)
d.left(135)
d.forward(145)
d.right(112)
d.forward(115)
d.left(137)
d.forward(163)
d.right(110)
d.forward(115)
d.left(130)
d.forward(142)
d.right(85)
d.forward(120)
d.left(130)
d.forward(128)
d.right(100)
d.forward(110)
d.left(126)
d.forward(115)
d.right(73)
d.forward(82)
d.left(136)
d.forward(60)

d.pensize(3)
d.left(70)
d.forward(15)
d.right(59)

def curve1(a,c):
    for i in range(c):
        d.right(a)
        d.forward(1)

def curve2(a,c):
    for i in range(c):
        d.left(a)
        d.forward(1)

curve1(0.1,260)
curve1(0.2,80)
d.left(6)
curve1(0.1,90)
d.right(60)
d.forward(11)
d.end_fill()


