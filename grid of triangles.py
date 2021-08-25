import turtle
import math
alex=turtle.Turtle()
wn=turtle.Screen()
def triangle(size,namturt):
    namturt.fillcolor('yellow') 
    namturt.begin_fill()    
    for n in range(3):
        namturt.forward(size)
        namturt.left(120)
    namturt.right(90)
    namturt.end_fill()
def boxoftriangles(size,namturt):
    for n in range(4):
        triangle(size,namturt)
        namturt.forward(size)
        namturt.right(180)
def rowofboxes(num,size,namturt):
    for n in range(num):
        boxoftriangles(size,namturt)
        namturt.forward(size+2*math.sin(math.radians(60))*size) 
def gridofboxes(numrow,numcol,size,namturt):
    for n in range(numrow):
        rowofboxes(numcol,size,namturt)
        namturt.right(90)
        namturt.forward(size+2*math.sin(math.radians(60))*size)
        namturt.left(90)
        namturt.backward(numcol*(size+2*math.sin(math.radians(60))*size))
size=50
numcol=10
numrow=10
alex.speed(10)
alex.backward(6*size)
alex.left(90)
alex.forward(6*size)
alex.right(90)
gridofboxes(numrow,numcol,size,alex)
wn.exitonclick()