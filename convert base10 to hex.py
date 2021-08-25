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
    
dig=int(input('enter integer'))
if dig<16 and dig>0:
    simple=numb_to_letter(dig)
    print(simple)

else:
    lines = list()
    #first find largest digit in hex-------------------------- need to make this into a for loop next..
 # for each hex digit, convert the base 10 of that digit to the number/letter corresponding to it
    for n in range(1,4):
        outer=int(dig/(pow(16,n)))
        while int(outer/16) > 16:
            outer=int(outer/16)
        else:
            if outer==16:
                lines.append(1)
            elif outer==0:
                print('end of program')
            else:
                lines.append(numb_to_letter(int(outer)))
        #rem=numb_to_letter(dig%16)
        #lines.append(rem)
        #dig = int(dig/16)
        
        #lines.append(numb_to_letter(int(dig/16)))
        #rem=numb_to_letter(dig%16)
        #lines.append(rem)
        #dig = int(dig/16)    
        #print('Your number in hex is:')
    print(lines)
    
    
    #A=10
    #B=11
    #C=12
    #D=13
    #E=14
    #F=15
#inp=int(input('enter a integer value in base 10'))
#num_tens=inp/16
#num_hundreds=num_tens/16
#digits=list()
#while inp>=16