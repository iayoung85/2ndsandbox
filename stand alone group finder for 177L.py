def takeattendance(masterstudentlist):
    attendancelist=list()
    for n in masterstudentlist:
        print(n)
        student=input('is he or she present? y/n')
        if student=='y':
            attendancelist.append(n)
    return attendancelist

def getnewnames(weeksfullattendance,masterstudentlist):
    namq=0
    while namq!='end':
        namq=input("Enter name of new student to add to list. type 'end' when finished")
        if namq!='end':
            weeksfullattendance.append(namq)
            masterstudentlist.append(namq)
    return weeksfullattendance

def makepair(weeksfullattendance):
    import random
    pair=list()
    for n in range(2):
        p1=random.randrange(len(weeksfullattendance))
        pair.append(weeksfullattendance[p1])
    return pair

def makerndmpairforweek(weeksfullattendance,mstrprevgrps):
    result=2
    while result==2:
        try:
            weeksgroups=list()
            for n in range(len(weeksfullattendance)//2):
                pair=['nobody','nobody']
                while (pair[0] or pair[1] not in weeksfullattendance) and (pair in mstrprevgrps or [pair[1],pair[0]] in mstrprevgrps) or pair[0]==pair[1]:
                    pair=makepair(weeksfullattendance)
                weeksgroups.append(pair)
                #print(pair)
                weeksfullattendance.remove(pair[0])
                weeksfullattendance.remove(pair[1])
            result=1
        except:
            result=2
            pass
    return weeksgroups

mstrprevgrps=[['nobody', 'nobody'], ['d', 'a'], ['b', 'c'], ['d', 'c'], ['a', 'b'], ['b', 'd'], ['a', 'c']]



masterstudentlist=['a', 'b', 'c', 'd']



print('ok, now lets see who is here from last week')
attendancelist=takeattendance(masterstudentlist)

print('is there anyone new to this class today?')
peoplepresent=getnewnames(attendancelist,masterstudentlist)
print('ok here is the attendance for this week')
print(peoplepresent)


#cllst=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t']
#print(len(cllst))
#mstrprevgrps=[['nobody','nobody'],['a','b'],['c','d'],['e','f'],['g','h'],['i','j'],['k','l'],['m','n'],['o','p'],['q','r'],['s','t']]

groupings=makerndmpairforweek(peoplepresent,mstrprevgrps)
print('here are the groupings for this week')
print(groupings)

mstrprevgrps.extend(groupings)
print('full list of all student groupings taken place thus far')
print(mstrprevgrps)

print('new list of all students to ever attend class')
print(masterstudentlist)
