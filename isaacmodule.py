#returns calculated pay assuming overtime hours are 1.5x normal pay
def computepay(hours_worked,pay_rate):
    if(float(hours_worked)<=40):
        return float(hours_worked)*float(pay_rate)
    else:
        return 40*float(pay_rate)+(1.5*(float(hours_worked)-40)*float(pay_rate))

# converts a number between 0 and 15 to hexadecimal
def numb_to_letter(numb):
    intnumb=int(numb)
    if intnumb==10:
        return 'A'
    if intnumb==11:
        return 'B'
    if intnumb==12:
        return 'C'
    if intnumb==13:
        return 'D'    
    if intnumb==14:
        return 'E'    
    if intnumb==15:
        return 'F'
    if intnumb<10 and intnumb>=0:
        return intnumb
#logic operator for converting base-10 to hexadecimal. 
def hexdig_or_false(inputval,power):
    intinputval=int(inputval)
    proc=float(intinputval/pow(16,power))
    if intinputval%pow(16,power)>=pow(16,power):
        return 'skip to next smallest power'
    elif proc>=1 and power!=1:
        return 'is a middle digit'
    elif proc==0 and power!=1:
        return 'is a middle digit'
    elif proc>=0 and power==1:
        return 'last 2 digits'
    elif proc>=0 and power!=1:
        return 'skip to next smallest power'
    else:
        #print('this is under zero')
        return 'falseunder'
#using hexdig_or_false() and numb_to_letter(), converts base-ten number to hex and prints the hex number in a list
def base_ten_to_hex(baseten):
    baseten=int(baseten)
    lines=list()
    for n in range(100,0,-1):
        proc=hexdig_or_false(baseten,n)
        if proc =='skip to next smallest power' and lines==[]:
            skiptosmallerpower=5
        elif proc =='skip to next smallest power' and lines!=[]:
            lines.append(numb_to_letter(int(baseten/pow(16,n))))
            baseten=baseten%pow(16,n)        
        elif proc =='is a middle digit':
            lines.append(numb_to_letter(int(baseten/pow(16,n))))
            baseten=baseten%pow(16,n)
        elif proc=='last 2 digits':
            sectolastdig=numb_to_letter(int(baseten/pow(16,n)))
            if lines!=[] and sectolastdig==0:
                lines.append(sectolastdig)
            elif sectolastdig!=0:
                lines.append(sectolastdig)
            finaldig=baseten%16
            lines.append(numb_to_letter(finaldig))
            baseten=-1
        else:
            print('this should not be happening error in hexdig_or_false')
    return lines
    #print(lines)    
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
#tells an object named alex to draw a star at each corner of a pentagon then move
def alex_make_pentagon(pentlength,starlength,alex):
    angle=360/5
    for n in range(5):
        alex.forward(pentlength)
        alex.left(angle)
        alex_make_star(starlength,alex,'red')
#makes a turtle named alex draw multiple layers of stars expanding outwards in a succeding number pentagons
def alex_make_layers_of_pentagons(pentlength,starlength,layers,alex):
    for n in range(0,layers):
        import math
        alex_make_pentagon(pentlength*(n+1),starlength,alex)
        alex.right(126)
        alex.forward((pentlength/2)/math.sin(math.radians(36)))
        alex.left(126)    
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

#makes a list of all factors of a given integer
def factor(integer):
    n=1
    listintsthatdivinteger=[]
    while integer>=n:
        if integer/n==integer//n:
            listintsthatdivinteger.append(n)
        n+=1
    return listintsthatdivinteger
  
#makes a list of integers which are coprime, smaller than, and greater than 0 to a given integer
def coprime(integer):
    intfactors=factor(integer)
    coprimelist=[]
    for n in range(1,integer):
        nfactor=factor(n)
        commonlist=[]
        for m in intfactors:
            if m in nfactor:
                commonlist.append(m)
        if commonlist==[1]:
            coprimelist.append(n)
    return coprimelist