#function that draws a row of n white stars
def makerowstars(namturt,height,numinrow):
    import math
    for n in range(numinrow):
        alex_make_star(0.0616*height*math.sin(math.radians(72)),namturt,'white')
        namturt.forward(2*0.063*height)
    namturt.right(90)
    namturt.forward(2*0.054*height)
    namturt.right(90)
    namturt.forward((numinrow)*2*0.063*height)
    namturt.right(180)
#tells a turtle object named alex to draw a 5 pointed star centered
def alex_make_star(size,alex,color):
    import math
    alex.fillcolor(str(color))    
    alex.begin_fill()
    alex.right(126)
    center=int((size/2)/math.sin(math.radians(72)))
    alex.forward(center)
    alex.left(162)
    for n in range(5):
        alex.forward(size)
        alex.left(144)
    alex.end_fill()
    alex.left(18)
    alex.forward(center)
    alex.right(54)    
#make a turtle draw a box
def make_box(height,width,color,namturt):
    namturt.fillcolor(color)
    namturt.begin_fill()
    for n in range(2):
        namturt.forward(width)
        namturt.right(90)
        namturt.forward(height)
        namturt.right(90)
    namturt.end_fill()
import turtle
import math
alex=turtle.Turtle()
wn=turtle.Screen()
height=500
width=1.9*height
alex.speed(0)
alex.pu()
alex.goto(-width/2,height/2)
alex.pd()
make_box(height,width,'white',alex)
alex.pu()
stripeht=height/13
for n in range(7):
    make_box(stripeht,width,'red',alex)
    alex.right(90)
    alex.forward(2*stripeht)
    alex.left(90)
alex.goto(-width/2,height/2)
make_box(7*height/13,0.76*height,'blue',alex)
alex.forward(0.063*height)
alex.right(90)
alex.forward(0.054*height)
alex.left(90)
for n in range(5):
    makerowstars(alex,height,6)
alex.goto(-width/2,height/2)
alex.seth(0)
alex.forward(2*0.063*height)
alex.right(90)
alex.forward(2*0.054*height)
alex.left(90)
for n in range(4):
    makerowstars(alex,height,5)
alex.hideturtle()
wn.exitonclick()
