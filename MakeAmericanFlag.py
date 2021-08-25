import turtle
import isaacmodule
import math
alex=turtle.Turtle()
wn=turtle.Screen()
height=500
width=1.9*height
stripecount=13
alex.speed(0)

if str(type(stripecount/2)) == "<class 'float'>":
    stripect=(stripecount+1)/2
else:
    stripect=stripecount/2

print('number of red stripes is: '+str(stripect))
alex.pu()
alex.goto(-width/2,height/2)
alex.pd()
isaacmodule.make_box(height,width,'white',alex)
alex.pu()
stripeht=height/(stripecount)
for n in range(int(stripect)):
    isaacmodule.make_box(stripeht,width,'red',alex)
    alex.right(90)
    alex.forward(2*stripeht)
    alex.left(90)
alex.goto(-width/2,height/2)
isaacmodule.make_box(7*height/13,0.76*height,'blue',alex)
alex.forward(0.063*height)
alex.right(90)
alex.forward(0.054*height)
alex.left(90)
for n in range(5):
    isaacmodule.makerowstars(alex,height,6)
alex.goto(-width/2,height/2)
alex.seth(0)
alex.forward(2*0.063*height)
alex.right(90)
alex.forward(2*0.054*height)
alex.left(90)
for n in range(4):
    isaacmodule.makerowstars(alex,height,5)
alex.hideturtle()
wn.exitonclick()
