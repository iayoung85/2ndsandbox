pentlength=int(input('enter length of pentagon'))
starlength=int(input('enter length of each star'))
layers=int(input('enter number of layers of stars to make'))
import isaacmodule
import turtle
import math
wn=turtle.Screen()
alex=turtle.Turtle()
alex.pu()
isaacmodule.alex_make_layers_of_pentagons(pentlength,starlength,layers,alex)
wn.exitonclick()