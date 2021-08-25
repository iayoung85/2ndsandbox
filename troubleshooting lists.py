grouphist=[['a', 'd'], ['c', 'b'], ['a', 'b'], ['d', 'c'], ['a', 'c'], ['b', 'd'], ['b', 'd'], ['a', 'c'], ['b', 'e'], ['a', 'd'], ['c', 'f'], ['d', 'join another group'], ['b', 'f'], ['c', 'g'], ['a', 'e'], ['c', 'd'], ['e', 'g'], ['a', 'f'], ['b', 'h'], ['a', 'b'], ['c', 'e'], ['d', 'f'], ['h', 'g'], ['e', 'd'], ['a', 'g'], ['b', 'c'], ['f', 'h'], ['e', 'b'], ['g', 'd'], ['a', 'h'], ['f', 'c']]

fullmatrix=[[['d', 'h'], ['b', 'f'], ['c', 'g'], ['a', 'e']], [['e', 'g'], ['c', 'd'], ['a', 'f'], ['b', 'h']], [['b', 'c'], ['a', 'g'], ['e', 'd'], ['f', 'h']], [['a', 'h'], ['e', 'b'], ['g', 'd'], ['f', 'c']], [['h', 'c'], ['g', 'b'], ['f', 'e'], ['a', 'd']], [['h', 'e'], ['g', 'f'], ['a', 'c'], ['d', 'b']], [['c', 'e'], ['h', 'g'], ['a', 'b'], ['d', 'f']]]
def repititions_in_arrangement(arrangement,all_groups):
    unique_list2=[]
    uniquegroupcountinweek=[]
    for n in all_groups:
        if n in unique_list2 or [n[1],n[0]] in unique_list2:
            thenonsense=0
        else:
            unique_list2.append(n)   
    for n in unique_list2:
        if n in arrangement or [n[1],n[0]] in arrangement:
            count=all_groups.count(n)+all_groups.count([n[1],n[0]])+1
            uniquegroupcountinweek.append(count)
    return uniquegroupcountinweek
def numuniquerepeatgroups_inlist(listofgroups,all_groups2):
    unique_list3=[]
    count=0
    for n in all_groups2:
        if n in unique_list3 or [n[1],n[0]] in unique_list3:
            thenonsense1=0
        else:
            unique_list3.append(n)   
    for t in unique_list3:
        if t in listofgroups or [t[1],t[0]] in listofgroups:
            count+=1
    return count
for n in fullmatrix:
    print(repititions_in_arrangement(n,grouphist))
    print(numuniquerepeatgroups_inlist(n,grouphist))
print(grouphist.count(['a', 'd']))