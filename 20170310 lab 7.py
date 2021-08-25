def bet2550inc(x):
    if x>=25 and x<=50:
        #print('your int is between 25 and 50 inclusive')
        return True
def strlen10to12(y):
    if len(y)==10 or len(y)==12:
        #print('your string is either 10 or 12 characters')
        return True
def times3lenstr(x,y):
    if x==3*len(y):
        #print('your string is 3*x characters long')
        return True
def lenstrnotdivby3(y):
    if len(y)%3!=0:
        #print('your string length is not a factor of 3')
        return True
def intisnegordivby3andeven(x):
    if x<0 or x%2==0 and x%3==0:
        #print('your int is neg or is even and div by 3')
        return True
#x=int(input('enter an integer'))
#y=input('enter a string')
def inttester(x):
    if bet2550inc(x) and  intisnegordivby3andeven(x):
        return True

def strtester(y):
    if strlen10to12(y) and lenstrnotdivby3(y):
        return True
def strinttester(x,y):
    if bet2550inc(x) and  intisnegordivby3andeven(x) and strlen10to12(y) and lenstrnotdivby3(y) and times3lenstr(x,y):
        return True
ones=0
twos=0
threes=0
fours=0
fives=0
sixes=0
sevens=0
eights=0
nines=0
tens=0
elevens=0
twelves=0
thirteens=0
fourteens=0
fifteens=0
sixteens=0
seventeens=0
eighteenorgreaters=0
import random
#x=0
#y=''
#numtries=0
#while strinttester(x,y)!=True:
    #x=random.randrange(-100,100)
    #y='x'*random.randrange(0,200)
    #numtries+=1
#print('the integer is',x,'and string length is',len(y),'and it took',numtries,'tries')
for n in range(50000):
    x=0
    y=1
    numtries=0
    while x != (y-6):
        x=random.randrange(1,7)
        y=random.randrange(7,13)
        numtries+=1
    #print('you got double', str(x)+ "'s! It took", numtries, 'rolls to get doubles this time!')
    if numtries==1 :
        ones+=1
    elif numtries==2:
        twos+=1
    elif numtries==3:
        threes+=1
    elif numtries==4:
        fours+=1
    elif numtries==5:
        fives+=1
    elif numtries==6:
        sixes+=1
    elif numtries==7:
        sevens+=1
    elif numtries==8:
        eights+=1
    elif numtries==9:
        nines+=1
    elif numtries==10:
        tens+=1
    elif numtries==11:
        elevens+=1
    elif numtries==12:
        twelves+=1
    elif numtries==13:
        thirteens+=1
    elif numtries==14:
        fourteens+=1
    elif numtries==15:
        fifteens+=1
    elif numtries==16:
        sixteens+=1
    elif numtries==17:
        seventeens+=1
    else:
        eighteenorgreaters+=1
import turtle
import isaacmodule
alex=turtle.Turtle()
wn=turtle.Screen()
histogram=[ones,twos,threes,fours,fives,sixes,sevens,eights,nines,tens,elevens,twelves,thirteens,fourteens,fifteens,sixteens,seventeens]
print(histogram)
alex.right(90)
alex.forward(500)
alex.left(90)
for n in histogram:
    alex.forward(20)
    alex.left(90)
    alex.forward(n//10)
    alex.left(90)
    alex.forward(20)
    alex.left(90)
    alex.forward(n//10)
    alex.left(90)
    alex.forward(20)
wn.exitonclick()
