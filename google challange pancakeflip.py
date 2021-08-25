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
def flip(S,K,P):
    cutout=S[P:K+P]
    if len(S)<K:
        print('Flipper too long for the pancake line')
        return False
    if P>len(S)-K:
        print('invalid flip position')
        return False
    flippedcutout=''
    for n in cutout:
        if n=='+':
            flippedcutout+='-'
        elif n=='-':
            flippedcutout+='+'
        else:
            print('invalid string')
            return False
    flippedS=S[0:P]+flippedcutout+S[K+P:]
    #print(flippedS)
    return flippedS


#given a string of +'s and -'s, returns the first string of homogeneous -'s that it finds
def consecminus(S):
    firststrminus=''
    for n in range(len(S)):
        if S[n]=='-':
            newstrtemp=S[n:]
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
    for n in range(len(S)):
        if S[n]=='-':
            return n
consecminus('+++-++---+-')
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
    for n in S:
        if n=='-':
            return False
    return True
def flipallfirstconsecminusk(S,K):
    flip=flipfirstconsecminusk(S,K)
    if flip==S and checkforminus(flip)==True:
        print('the pattern is totally complete no more minus signs'+flip)
        return flip
    prvflip=''
    while flip!='not' and flip!=prvflip:
        prvflip=flip
        flip=flipfirstconsecminusk(flip,K)
    if flip==prvflip and checkforminus(flip)==True:
        print('the pattern is complete no more minus signs'+flip)
        return flip
    if flip==prvflip and checkforminus(flip)==False:
        print('job completed: '+flip)
        return flip
#skips a set of minus signs to search for minus signs afterbarrier.
def removeintminusgroup(flip,K):
    if checkforminus(flip)==False:
        cutpoint=lastpos(flip)
        newstrafter=flip[cutpoint:]
        print('newstrafter is'+newstrafter)
        befnewst=flip[:cutpoint]
        print('befnewst is'+befnewst)
        straftertoconcat=flipallfirstconsecminusk(newstrafter,K)
        flip=befnewst+straftertoconcat
        print('after skipping the first set of minuses too short, flipped after that: '+flip)
    return flip
#returns false if there are no groups of minus signs of K length or greater in a string returns True if there are groups of minus signs of K length or greater
def checkkthminusgrp(S,K):
    while len(consecminus(S))<K and checkforminus(S)==False:
        cutpoint=lastpos(S)
        S=S[cutpoint:]
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
        finalstr+=flippered[:lastpos(flippered)]
        flippered=flippered[lastpos(flippered):]
        if checkkthminusgrp(flippered,K)==False:
            finalstr+=flippered
            flipped=finalstr
    print('after removing groups of klength minus: '+flipped)
    return flipped
removegroupsofminus('------',6)

#takes a string s which has no groups of minus signs larger than K and condenses it to one group of minus signs
def minuscongeal(S,K):
    for n in S:
        if n=='-':
            flipped=flip(S,K,findP(S))
            return flipped
print(minuscongeal('-+++++-',3))

#counts number of minus islands in string
def islandcounter(S):
    counter=0
    #if S!=False:
    for n in range(len(S)-1):
        if S[n]!=S[n+1]:
            counter+=1
    counter=counter//2+counter%2
    if S[0]=='-':
        counter+=1
    print('number of minus islands is: '+str(counter))
    return counter
def completeflippingprogram(S,K):
    S=removegroupsofminus(S,K)
    while islandcounter(S)>1:
        S=minuscongeal(S,K)
    lastisland=S[findP(S):lastpos(S)]
    if len(lastisland)==K and islandcounter(S)==1:
        S=S[:findP(S)]+('+'*K)+S[lastpos(S):]
    return S

print(completeflippingprogram('-++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-',2))