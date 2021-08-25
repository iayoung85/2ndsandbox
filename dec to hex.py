#program is designed to convert any integer greater than 0 to hexadecimal
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
print("type 'exit' to leave program")
baseten=0
while baseten!='exit':
    try:
        baseten=int(input('enter integer'))
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
                print('this should not be happening')
        print(''.join(map(str,lines)))
        #print(lines)
    except:
        question=input('do you want to exit? y/n')
        if question=='y':
            baseten='exit'
        else:
            print('ok try again!')