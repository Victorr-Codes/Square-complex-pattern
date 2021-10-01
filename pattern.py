import turtle
t = turtle.Turtle()

s = turtle.Screen()
s.bgcolor("black")
t.pencolor("white")
t.speed(0)
c = 0
d = 0
while 1:
    for i in range(4):
        t.forward(80)
        t.right(90)
    t.right(30)
    c += 1
    if c >= 390 / 30:
        t.forward(50)
        c = 0
        d += 1
        if d >= 12:
            break

t.hideturtle()
turtle.done()
