def generaterandomsolution(lenofsolution,charsallowed):
    if lenofsolution>int(len(charsallowed)):
        print('unable to generate random solution, not enough characters')
    else:
        try:
            import random
            solution=''
            randomchar=random.randrange(int(len(charsallowed)))
            for n in range(lenofsolution):
                while charsallowed[randomchar] in solution:
                    charsallowed=charsallowed[0:randomchar]+charsallowed[randomchar+1:int(len(charsallowed))]
                    randomchar=random.randrange(int(len(charsallowed)))
                solution+=charsallowed[randomchar]
            return solution
        except:
            print('there are not enough UNIQUE characters in your string of possible characters to generate a solution')
def difficultylevel(charsallowed,solutionlength,grange):
    import math
    numposssolutions=math.factorial(solutionlength)
    gamediff=((int(len(removenonunique(charsallowed)))*numposssolutions-1)/grange)
    return gamediff
def removenonunique(charsallowed):
    shortened=''
    for n in range(int(len(charsallowed))):
        if charsallowed[n] not in shortened:
            shortened=shortened+charsallowed[n]
            #print(shortened,charsallowed)
    return shortened
def guesscheck(currentguess,charsallowed,solutionlength,glist):
    for m in currentguess:
        if m not in charsallowed:
            return False
    if int(len(currentguess))!=solutionlength:
        return False
    if currentguess in glist:
        return False
    else:
        return True
def countnumcorrect(currentguess,solution):
    numcorr=0
    for n in range(int(len(currentguess))):
        if currentguess[n]==solution[n]:
            numcorr+=1
    return (str(numcorr)+' characters placed correctly')
def countnummissplaced(currentguess,solution):
    nummissplaced=0
    for n in range(int(len(currentguess))):
        if currentguess[n]!=solution[n] and currentguess[n] in solution:
            nummissplaced+=1
    return(str(nummissplaced)+' characters are correct identity but wrong spot')
grange=0
while grange==0:
    grange=input('How many guesses do you want? ')
    try:
        grange=int(grange)
        if grange==0:
            print('please make it an integer above 0!')
        while grange<0:
            print('it must be a positive number')
            grange=0
    except:
        print('Sorry, you must enter an integer, try again!')
        grange=0
def getsolutionlength():
    solutionlength=0
    while solutionlength==0 or solutionlength>94:
        solutionlength=input('How long do you want the solution to be? ')
        try:
            solutionlength=int(solutionlength)
            if solutionlength>0 and solutionlength<95:
                return solutionlength
            else:
                print('Your answer must be greater than 0 and less than 95 because there are only 94 unique characters on your keyboard!')
                solutionlength=0
        except:
            print('Sorry, you must enter an integer, try again!')
            solutionlength=0
def getguess(n,solutionlength,charsallowed):
    currentguess=input('Enter guess #'+str(n+1)+' of length '+str(solutionlength)+' made from unique characters in choice pool: '+removenonunique(charsallowed)+': ')
    return currentguess
solutionlength=getsolutionlength()
charsallowed=input('Enter a string of unique characters to use as a set of choices for your guesses. ')
while solutionlength>int(len(removenonunique(charsallowed))):
    print('You need to either enter a shorter solution length or increase the number of unique characters in your pool of choices.')
    print('please try again')
    solutionlength=getsolutionlength()
    charsallowed=input('Enter a string of unique characters to use as a set of choices for your guesses. ')    

glist=[]
gdetaillist=[]
for n in range(grange):
    glist.append('-'*solutionlength)
for n in range(grange):
    gdetaillist.append(' guess #'+str(n+1))
solution=generaterandomsolution(solutionlength,charsallowed)
#print(solution)
for n in range(grange):
    currentguess=getguess(n,solutionlength,charsallowed)
    while currentguess=='haxorcheat':
        print('the solution is:',solution)
        currentguess=getguess(n,solutionlength,charsallowed)        
    while guesscheck(currentguess,charsallowed,solutionlength,glist)==False:
        print('Sorry but your guess does not conform to the rules of the game, enter a valid guess')
        currentguess=getguess(n,solutionlength,charsallowed)
    glist[n]=currentguess
    gdetaillist[n]='guess #'+str(n+1)+'. '+countnumcorrect(currentguess,solution)+' and '+countnummissplaced(currentguess,solution)
    if currentguess==solution:
        if n==0:
            print('OMG YOU MUST BE CHEATING!!! HOW DID IT ONLY TAKE YOU 1 GUESS?!?!')
            numtries=1
            break
        else:
            print('CONGRATULATIONS! It took you '+str(n+1)+' guesses to find the solution!')
            numtries=1+n
            break
    for n in range(grange-1,-1,-1):
        print(glist[n],gdetaillist[n])
if currentguess!=solution:
    print("I'm sorry but YOU LOST!!! HAHAHAAH the answer was: " +solution)
    numtries=0
nameofplayer=input('for the recordbook, what is your name?')
difflevel=difficultylevel(charsallowed,solutionlength,grange)
print('Your difficulty level (meaning your score if you needed all guesses) was: '+str(difflevel)+' uniquechars*possiblesolutions/guess')
if numtries==0:
    playerscore=0
    print('Your score was 0')
if numtries>0:
    playerscore=((1+grange-numtries)*difflevel)//1
    print('Your score was: '+str(playerscore))
