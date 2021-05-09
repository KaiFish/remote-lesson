import turtle
import functions as f

t = f.getTurtle() #get turtle from functions
t.shape("turtle")
s = t.getscreen()
s.bgcolor("CornflowerBlue")

# s.tracer(20)        # uncomment to make animation go fast
t.color("ForestGreen")
t.pu()
t.goto(-420,-200)
t.pd()
# draw grass 830x185

t.color("FireBrick")
t.pu()
t.goto(-200,-200)
t.pd()
# draw house 300x400

t.pu()
t.color("deepSkyBlue")
t.goto(-150, -125)
t.pd()
# draw window1 125x75

t.pu()
t.goto(150, -125)
t.pd()
# draw window2 125x75

t.pu()
t.color("SaddleBrown")
t.goto(-50,-200)
t.pd()
# draw door 200x100

t.pu()
t.color("Gold")
t.goto(50, -100)
t.fd(5)
t.seth(90)
t.pd()
t.begin_fill()
t.circle(5)     #draw door knob
t.end_fill()

t.pu()
t.color("slateGray")
t.goto(-275,100)
t.pd()
# draw roof - isosceles with base 550, angles 30,30,120

t.goto(125, 125)
t.seth(90)
# draw chiminey 85x75

t.pu()
t.color("whitesmoke")       #draw chiminey smoke
t.goto(175, 250)
t.pd()
f.spiral(5, 20)
t.pu()
t.goto(225,275)
t.pd()
f.spiral(5, 20)
t.pu()
t.goto(290,300)
t.pd()
f.spiral(5, 20)

t.pu()
t.goto(-315,225)
t.pd()
# draw sun

t.pu()
t.goto(-100,300)
t.pd()
# draw cloud size 50

t.pu()
t.goto(-160,-220)
t.pd()
# draw bush 1 r = 12

t.pu()
t.goto(342,-220)
t.pd()
#draw bush 2 r = 12

t.pu()
t.color("Gold")
t.seth(90)
t.goto(0,15)    #place turtle above door

s.update()
turtle.done()
