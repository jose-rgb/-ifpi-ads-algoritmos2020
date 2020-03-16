import turtle
import math
jose = turtle.Turtle()


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)


def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)


def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)


def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()


move(jose, -100)
flower(jose, 7, 60.0, 60.0)

move(jose, 100)
flower(jose, 10, 40.0, 80.0)

move(jose, 100)
flower(jose, 20, 140.0, 20.0)

jose.hideturtle()
turtle.mainloop()