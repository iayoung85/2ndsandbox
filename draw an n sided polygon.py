sides=int(input('how many sides is your polygon? '))
length=int(input('how long do you want each side to be? '))
import turtle
import math
wn=turtle.Screen()
alex=turtle.Turtle()

for n in range(0,sides):
    alex.forward(length)
    alex.left(180-(180*(sides-2))/sides)
wn.exitonclick()