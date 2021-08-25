#T is the number(integer) of test cases
#K is the length (integer) of the pancake flipper
#S is the line of pancakes randomly up or down (string of + and - symbols)
#if K is greater than length of S, impossible
#count is number (integer) of flips of the pancake flipper required to complete the task.

#first find and flip any group of - where length of the group is equal to a multiple of K. add len(-)/K to count
#repeat below two steps until either all + or a single group of - exists. 
#when only 1 group of - exists that cannot be flipped by one K, report impossible
#next systematically from left to right, flip groups of - with length equal to K. add 1 to count for each flip.
#from left to right, find first - and then flip that - plus the next k-1 characters after that -. add 1 to count.
#scan for groups of - with length equal to K and flip, add 1 to count for each flip.

#function that flips a string of K length from within a string, S. Does this at position "P" (integer between 0 and length(S)-k) K must be less than S
def flip(Slist,K,P):
    S=Slist[0]
    glblct=int(Slist[1])
    LMO=len(S)
    if LMO<K:
        print('Flipper too long for the pancake line')
        return False
    if P>LMO-K:
        print('invalid flip position')
        return False
    cutout=S[P:K+P]
    flippedcutout=''
    for n in cutout:
        if n=='+':
            flippedcutout+='-'
        elif n=='-':
            flippedcutout+='+'
        else:
            print('invalid string')
            return False
    glblct+=1
    flippedS=[S[0:P]+flippedcutout+S[K+P:],glblct]
    #print(flippedS)
    return flippedS


#given a string of +'s and -'s, returns the first string of homogeneous -'s that it finds
def consecminus(S):
    firststrminus=''
    pancakes=S[0]
    for n in range(len(pancakes)):
        if pancakes[n]=='-':
            newstrtemp=pancakes[n:]
            if newstrtemp[len(newstrtemp)-1]=='-' and '+' not in newstrtemp:
                print('the only string of minus signs is at the end and is: '+newstrtemp)
                return newstrtemp
            for m in newstrtemp:
                if m=='-':
                    firststrminus+='-'
                elif m=='+':
                    print('firststrminus: '+firststrminus)
                    return firststrminus
    print('there were no minus signs in string')
    return 'finished'

#returns the position, P, of the first string of minuses in string S
def findP(S):
    for n in range(len(S[0])):
        if S[0][n]=='-':
            return n
#finds the posiiton of the last '-' in the first string of minuses in string S
def lastpos(S):
    P=findP(S)
    length=len(consecminus(S))
    lastposition=P+length
    return lastposition
#flips the first str of minus signs of appropriate length greater than or equal to K or else returns not
def flipfirstconsecminusk(S,K):
    csminus=consecminus(S)
    if csminus!='finished':
        if len(consecminus(S))>=K:
            P=findP(S)
            flipped=flip(S,K,P)
            return flipped
        else:
            return S
    if csminus=='finished':
        return S
def checkforminus(S):
    pancakes=S[0]
    for n in pancakes:
        if n=='-':
            return False
    return True
def flipallfirstconsecminusk(S,K):
    flip=flipfirstconsecminusk(S,K)
    if flip==S and checkforminus(flip)==True:
        print('the pattern is totally complete no more minus signs'+str(flip))
        return flip
    prvflip=''
    while flip[0]!='not' and flip[0]!=prvflip:
        prvflip=flip[0]
        flip=flipfirstconsecminusk(flip,K)
    if flip[0]==prvflip and checkforminus(flip)==True:
        print('the pattern is complete no more minus signs'+str(flip))
        return flip
    if flip[0]==prvflip and checkforminus(flip)==False:
        print('job completed: '+str(flip))
        return flip
#skips a set of minus signs to search for minus signs afterbarrier.
def removeintminusgroup(flip,K):
    if checkforminus(flip)==False:
        cutpoint=lastpos(flip)
        newstrafter=flip[0][cutpoint:]
        print('newstrafter is'+str(newstrafter))
        befnewst=flip[0][:cutpoint]
        print('befnewst is'+str(befnewst))
        straftertoconcat=flipallfirstconsecminusk([newstrafter,flip[1]],K)
        flippedstr=befnewst+straftertoconcat[0]
        flip=[flippedstr,straftertoconcat[1]]
        print('after skipping the first set of minuses too short, flipped after that: '+str(flip))
    return flip

#returns false if there are no groups of minus signs of K length or greater in a string returns True if there are groups of minus signs of K length or greater
def checkkthminusgrp(S,K):
    while len(consecminus(S))<K and checkforminus(S)==False:
        cutpoint=lastpos(S)
        S=[S[0][cutpoint:],S[1]]
    if checkforminus(S)==True:
        print('no more minus signs')
        return False
    else:
        return True

def removegroupsofminus(S,K):
    flipped=flipallfirstconsecminusk(S,K)
    finalstr=''
    flippered=flipped
    while checkkthminusgrp(flippered,K)==True:
        flippered=removeintminusgroup(flippered,K)
        finalstr+=flippered[0][:lastpos(flippered)]
        flippered=[flippered[0][lastpos(flippered):],flippered[1]]
        if checkkthminusgrp(flippered,K)==False:
            finalstr+=flippered[0]
            flipped=[finalstr,flippered[1]]
    print('after removing groups of klength minus: '+str(flipped))
    return flipped

#takes a string s which has no groups of minus signs larger than K and condenses it to one group of minus signs
def minuscongeal(S,K):
    for n in S[0]:
        if n=='-':
            flipped=flip(S,K,findP(S))
            return flipped

#counts number of minus islands in string
def islandcounter(S):
    counter=0
    #if S!=False:
    for n in range(len(S[0])-1):
        if S[0][n]!=S[0][n+1]:
            counter+=1
    counter=counter//2+counter%2
    if S[0][0]=='-':
        counter+=1
    print('number of minus islands is: '+str(counter))
    return counter
def completeflippingprogram(S,K):
    S=removegroupsofminus(S,K)
    while islandcounter(S)>1:
        S=minuscongeal(S,K)
    if islandcounter(S)==1:
        if len(S[0][findP(S):lastpos(S)])==K:
            S=[S[0][:findP(S)]+('+'*K)+S[0][lastpos(S):],S[1]+1]
    return S
#print(flipallfirstconsecminusk(['------',0],3))
#print(consecminus(['-----',0]))
#print(checkforminus(['+++++-+',0]))
#print(removeintminusgroup(['---+------',0],3))
#print(minuscongeal(['---',0],3))

#print(removegroupsofminus(['---+-+--',0],3))

#print(removegroupsofminus(['----+----',0],3))
#print(islandcounter(['-----',0]))
print(completeflippingprogram(['++++++++---+-----+++--+++++',0],5))
