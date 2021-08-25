#input a list of students present this week, and a list of all groups that have occurred before and returns a list of pairs for this week.
#if the number of students present in a week is odd, assigns 3rd person to the last pair of the week.
def assigngroups(attendancelist,prvgroups):
    import random
    poplist=[]
    while len(attendancelist)%2!=0:
        alltrips=removeineltrips(makealltriplets(attendancelist),prvgroups)
        if alltrips==[]:
            print('there were no remaining triplet groups to pick where the rule of no repeating partners may be followed, choosing a random repeated triple group')
            return 'nojoy1'
        else:
            poplist.append(alltrips[random.randrange(len(alltrips))])
        attendancestorage=[]
        for n in range(len(attendancelist)):
            attendancestorage.append(attendancelist[n])
        attendancelist=[]
        for n in range(len(attendancestorage)):
            if attendancestorage[n] not in poplist[0]:
                attendancelist.append(attendancestorage[n])
    allpairs=removeprevpairs(makeallpairs(attendancelist),populatedoubles(prvgroups))
    if allpairs==[]:
        print('there were no more remaining possible pairs that follow the no repeating partners rule, choosing a random repeated double group')
        return 'nojoy2'
    else:
        for n in range(int(len(attendancelist)//2)):
            try:
                randpai=allpairs[random.randrange(len(allpairs))]
            except:
                print('there were no more remaining possible pairs that follow the no repeating partners rule, choosing a random repeated double gorup')
                renewpairs=makeallpairs(attendancelist)
                randpai=renewpairs[random.randrange(len(renewpairs))]
                poplist.append(randpai)
                #return 'nojoy3'                
            allpairs=removenames(allpairs,randpai)
            #if allpairs==[] and len(poplist)!=len(attendancelist)//2:
                #print('there were no more remaining possible pairs that follow the no repeating partners rule, choosing a random repeated double gorup')
                #return 'nojoy3'
            #else:
            poplist.append(randpai)
        return poplist

#asks which students are present and populates a new list containing only present students
def takeattendance(masterstudentlist):
    present=list()
    for n in masterstudentlist:
        print(n)
        student=input('is he or she present? y/n')
        if student=='y':
            present.append(n)
    return present

#adds new students to the list of present students and the list of all students that have ever attended
def getnewnames(weeksfullattendance,masterstudentlist):
    namq=0
    while namq!='end':
        namq=input("Enter name of new student to add to list. type 'end' when finished")
        if namq!='end':
            weeksfullattendance.append(namq)
            masterstudentlist.append(namq)
    return weeksfullattendance

#makes a list of all names in all prevgroups for only those who are present
def makelist(attendancelist,prevgroups):
    numtimes=[]
    for n in prevgroups:
        for m in n:
            if m in attendancelist:
                numtimes.append(m)
        
#arranges names on an attendance list according to the total # of different groups that they have been a part of
#largest # of times first

    
#makes a pair of separate items from a list
def makepair(anylist):
    import random
    pair=[]
    nl=[]
    for n in range(len(anylist)):
        nl.append(anylist[n])
    for n in range(2):
        p1=random.randrange(len(nl))
        pair.append(nl[p1])
        del(nl[p1])
    return pair

#make a list of all possible pairings from a set of students in a list
def makeallpairs(anylist):
    listofpairs=[]
    for n in range(len(anylist)):
        for m in range(len(anylist)):
            if n!=m and [anylist[n], anylist[m]] not in listofpairs and [anylist[m],anylist[n]] not in listofpairs:
                listofpairs.append([anylist[n], anylist[m]])
    return listofpairs

#remove previous pairings from list of all possible pairings
def removeprevpairs(allposspairs,prevgroups):
    trips=populatetrips(prevgroups)
    doubles=populatedoubles(prevgroups)
    excludedoubles=[]
    for n in allposspairs:
        if n not in doubles and [n[1],n[0]] not in doubles:
            excludedoubles.append(n)
    if len(trips)>=1:
        for m in trips:
            try:
                excludedoubles.remove([m[0],m[1]])
                excludedoubles.remove([m[1],m[0]])
                excludedoubles.remove([m[2],m[1]])
                excludedoubles.remove([m[1],m[2]])
                excludedoubles.remove([m[0],m[2]])
                excludedoubles.remove([m[2],m[0]])
            except:
    
                return excludedoubles
    else:
        return excludedoubles



#removes all groups from list that contain a name
def removename(listofgroups,name):
    newlist=[]
    for n in listofgroups:
        if str(name) != str(n):
                newlist.append(n)
    return newlist

#removes each name in a group from a list of groups
def removenames(listofgroups,group):
    remakelist=[]
    for n in listofgroups:
        remakelist.append(n)
    for n in group:
        remakelist=removename(remakelist,n)
    return remakelist

#get a list of all triplets from the master list of previous groups
def populatetrips(allprevgroups):
    poptrips=[]
    for n in allprevgroups:
        if len(n)==3:
            poptrips.append(n)  
    return poptrips

#make a list of all pairs from the master list of previous groups
def populatedoubles(allprevgroups):
    popdoubs=[]
    for n in allprevgroups:
        if len(n)==2:
            popdoubs.append(n)
    return popdoubs

#remove all ineligible triplets from the population of all triplets.
def removeineltrips(allposstrips,prevgroups):
    excludetrips=[]
    trips=populatetrips(prevgroups)
    doubles=populatedoubles(prevgroups)
    for n in allposstrips:
        if n not in trips and [n[1],n[0],n[2]] not in trips and [n[2],n[0],n[1]] not in trips and [n[2],n[1],n[0]] not in trips and [n[0],n[2],n[1]] not in trips and [n[1],n[2],n[0]] not in trips:
            excludetrips.append(n)
    excludedoubles=[]
    for n in excludetrips:
        if [n[0],n[1]] not in doubles and [n[1],n[0]] not in doubles and [n[0],n[2]] not in doubles and [n[2],n[0]] not in doubles and [n[1],n[2]] not in doubles and [n[2],n[1]] not in doubles:
            excludedoubles.append(n)
    return excludedoubles 

#make a list of all possible 3-person groups from a set of students in a list
def makealltriplets(anylist):
    listoftrips=[]
    for n in range(len(anylist)):
        for m in range(len(anylist)):
            for l in range(len(anylist)):
                if n!=m and n!=l and m!=l and [anylist[n],anylist[m],anylist[l]] not in listoftrips and [anylist[l],anylist[n],anylist[m]] not in listoftrips and [anylist[m],anylist[l],anylist[n]] not in listoftrips and [anylist[n],anylist[l],anylist[m]] not in listoftrips and [anylist[m],anylist[n],anylist[l]] not in listoftrips and [anylist[l],anylist[m],anylist[n]] not in listoftrips:
                    listoftrips.append([anylist[n],anylist[m],anylist[l]])
    return listoftrips

#makes a list of all possible groups of 3 and then picks one at random
def selecttriplet(attendancelist,previousgroups):
    import random
    alltriplets=makealltriplets(attendancelist)
    excludeused=removeineltrips(alltriplets,previousgroups)
    if excludeused==[]:
        return 'notrips'
    group=excludeused[random.randrange(len(excludeused))]
    return group

#makes a list of all possible groups of 2 and then picks one at random
def selectranpair(attendancelist,prevgroups):
    import random
    allpairs=makeallpairs(attendancelist)
    excludeused=removeprevpairs(allpairs,prevgroups)
    if excludeused==[]:
        return 'nopairs'
    group=excludeused[random.randrange(len(excludeused))]
    return group

def logicselectranpair(attendancelist,prevgroups):
    import random
    allpairs=makeallpairs(attendancelist)
    excludeused=removeprevpairs(allpairs,prevgroups)
    for n in range(10):
        try:
            group=excludeused[random.randrange(len(excludeused))]
            if removenames(attendancelist,group) not in prevgroups:
                return group
        except:
            return 'nopairs'
    return 'nopairs'

def makethisweeksgroups(attendance,usedgroups):
    thisweeksgroups=[]
    if len(attendance)%2==1:
        triplet=selecttriplet(attendance,usedgroups)
        if triplet=='notrips':
            return 'nomore'
        tripletremoved=removenames(attendance,triplet)
        thisweeksgroups.append(triplet)
        thisweeksgroups=makepairs(attendance,usedgroups,thisweeksgroups)
        return thisweeksgroups
    else:
        thisweeksgroups=makepairs(attendance,usedgroups,thisweeksgroups)
        return thisweeksgroups

def makepairs(listnames,usedgroups,currgrplist):
    numstudents=len(listnames)
    for n in range(numstudents//2):
        if len(listnames)>4:
            pair=selectranpair(listnames,usedgroups)
        else:
            pair=logicselectranpair(listnames,usedgroups)
        if pair=='nopairs':
            return 'nomore'
        listnames=removenames(listnames,pair)
        usedgroups.append(pair)
        currgrplist.append(pair)   
    return currgrplist    
#since I cannot find a solid way to make it work every time, i need to have the program guess and check...
def makegroups(attendance,usedgroups):
    for n in range(20):
        try:
            weeksgrps=makethisweeksgroups(attendance,usedgroups)
            return weeksgrps
        except:
            print('haha you had an exception')
            return 'nomore'
def makegroupstocompletion(attendance,usedgroups):
    makegrps=[]
    allweeksgroups=[]
    counter=0
    while makegrps!='nomore':
        makegrps=makegroups(attendance,usedgroups)
        #print(len(makegrps))
        if makegrps!='nomore':
            #for n in makegrps:
                #usedgroups.append(n)
            counter+=1
            allweeksgroups.append(makegrps)
            print(allweeksgroups)
            print(len(allweeksgroups))
    return counter
#attendance=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
#usedgroups=[['a','b'],['b','c'],['c', 'd'], ['b', 'g'], ['a', 'f'], ['e', 'h'],['b', 'e'], ['a', 'd'], ['f', 'h'], ['c', 'g'],['c', 'e'], ['b', 'd'], ['f', 'g'], ['a', 'h'],['d', 'e'], ['g', 'h'], ['a', 'c'], ['b', 'f']]


#print(attendance)
#print(selectranpair(attendance,usedgroups))
#print(makethisweeksgroups(attendance,usedgroups))
attemptgram=[]
histogramattempts=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for n in range(500):
    usedgroups=[]
    attendance=list(map(str,list(range(12))))
    numattempts=makegroupstocompletion(attendance,usedgroups)
    histogramattempts[numattempts]+=1
    if numattempts not in attemptgram:
        attemptgram.append(numattempts)
print(attemptgram)
print(histogramattempts)
#import random
#for n in range(1000):
    #attendance=list(range(random.randrange(8,30)))
    #attendance=list(map(str,attendance))
    

#print(removenames([['A', 'AA'], ['A', 'AAA']],['AAA','AA']))
#for n in range(10):
    #print(logicselectranpair(['a', 'b', 'c', 'd'],[['a', 'b'],['c', 'd'],['a','d'],['b','c']]))
    