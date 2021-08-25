def alex_make_star(size):
    alex.fillcolor('red')    
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
    #alex.reverse(center)    
def alex_make_pentagon(pentlength,starlength):
    angle=360/5
    for n in range(5):
        alex.forward(pentlength)
        alex.left(angle)
        alex_make_star(starlength)
pentlength=int(input('enter length of pentagon'))
starlength=int(input('enter length of each star'))
import turtle
import math
wn=turtle.Screen()
alex=turtle.Turtle()
alex.pu()
layers=int(input('enter number of layers of stars to make'))
for n in range(0,layers):
    alex_make_pentagon(pentlength*(n+1),starlength)
    alex.right(126)
    alex.forward((pentlength/2)/math.sin(math.radians(36)))
    alex.left(126)
wn.exitonclick()