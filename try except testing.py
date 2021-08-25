x=float(input('enter a number'))
try:
    x+=1
    print('this is an integer')
except TypeError:
    print('this worked')