import turtle
import random as r


c = ["Blue", "DarkViolet", "DeepPink", "ForestGreen", "FireBrick", "DarkOrange", "Yellow"]

t = turtle.Turtle()

def getTurtle():
    return t

def triangle(side):
    for i in range(3):
        t.fd(side)
        t.lt(120)

def square(side):
    for i in range(4):
        t.fd(side)
        t.lt(90)

def hexagon(side):
    for i in range(6):
        t.fd(side)
        t.lt(60)

def spiral(radius, x):
    for i in range(x):
        t.circle(radius + i, 45)

def randColor():
    t.color(r.choice(c))

def movePen(x):
    t.pu()
    t.fd(x)
    t.pd()

def rect(l, w):
    t.fd(l)
    t.rt(90)
    t.fd(w)
    t.rt(90)
    t.fd(l)
    t.rt(90)
    t.fd(w)


def leaf(d):        #d = direction
    if d == "l":    #left
        r = 60      #radius
        a = 95      #angle
    elif d == "r":  #right
        r = -60
        a = -95
    t.color("DarkGreen")
    t.begin_fill()
    t.circle(r, 85)
    t.lt(a)
    t.circle(r, 85)
    t.end_fill()

def petal(r, a, c):      # r = radius, a = angle, c = arC
    t.begin_fill()
    t.circle(r, c)
    t.lt(a)
    t.circle(r, c)
    t.end_fill()

def cloud(s):       # s = size
    t.color("white")
    t.seth(270)
    t.begin_fill()
    t.circle(s)
    t.end_fill()
    t.seth(180)
    t.bk(s/2)
    t.seth(270)
    t.begin_fill()
    t.circle(-s)
    t.end_fill()
    t.seth(90)
    t.fd(s*.9)
    t.seth(0)
    t.fd(s/2)
    t.seth(90)
    t.begin_fill()
    t.circle(s*.8)
    t.end_fill()
    t.seth(270)
    t.pu()
    t.fd(5*s/4)
    t.pd()
    t.begin_fill()
    t.circle(-s*.7)
    t.end_fill()

def sun():
    t.seth(270)
    t.color("DarkOrange")
    for i in range(22):
        petal(40, 95, 60)
        t.rt(195)
    t.color("Gold")
    t.seth(0)
    t.fd(5)
    t.seth(90)
    t.fd(5)
    t.begin_fill()
    t.circle(55)
    t.end_fill()

def bush(r):    # r = radius of bumps on bush
    t.color("DarkGreen")
    t.seth(0)
    t.begin_fill()
    for i in range(13):
        t.circle(r, 180)
        t.lt(195)
    t.seth(0)
    print(t.pos())
    t.fd(r*15.1)
    t.end_fill()
