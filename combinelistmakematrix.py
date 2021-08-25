def combinelistwithself(list1,list2):
    matrix=[]
    for n in list1:
        sublist=[]
        for m in list2:
            grp=[n,m]
            #print(grp)
            sublist.append(grp)
        matrix.append(sublist)
    return matrix

#remove pairs in a matrix where the pair is made up of only one person
def removedups(matrix):
    for n in matrix:
        for m in n:
            if m[0]==m[1]:
                n.remove(m)
    return matrix

def determinelocation(matrix,pair):
    for m in matrix:
        if pair in m:
            row=matrix.index(m)
            column=m.index(pair)
    return [row,column]

def removerowandcolumn(matrix,pair):
    makenewmatrix=[]
    for n in matrix:
        makenewmatrix.append(n)
    if makenewmatrix==[]:
        return 'finished'
    loc=determinelocation(makenewmatrix,pair)
    makenewmatrix.remove(matrix[loc[0]])
    for n in makenewmatrix:
        n.remove(n[loc[1]])
    return makenewmatrix

def removegroup(matrix,pair):
    totallynewmatrix=removerowandcolumn(matrix,pair)
    newermatrix=removerowandcolumn(totallynewmatrix,[pair[1],pair[0]])
    return newermatrix

#populate a list of groups that excludes previous groups.
def populateset(listn,prvgrps):
    listm=[]
    #print(listn)
    for n in listn:
        if n not in prvgrps and [n[1],n[0]] not in prvgrps:
            listm.append(n)
    #print(listm)
    return listm
#given a matrix, returns a list of items from matrix, combines lines of matrix into list
def matrixlinear(matrix):
    listn=[]
    for m in matrix:
        for n in m:
            listn.append(n)
    return listn
#rather than picking a random group from a matrix, it will be better to pick a random group from a list made from that matrix then redress the original matrix to remove nonused items
def pickrandom(matrix,prvgrps):
    listn=populateset(matrixlinear(matrix),prvgrps)
    import random
    choice=listn[random.randrange(len(listn))]
    for n in range(25):
        if choice[0]!=choice[1]:
            return choice
        else:
            choice=listn[random.randrange(len(listn))]
    

#makes a complete set of orthogonal groups from a matrix
def makegroupset(matrix,prvgrps):
    width=int(len(matrix[0]))
    groupset=[]
    for n in range(width//2):
        group=pickrandom(matrix,prvgrps)
        matrix=removegroup(matrix,group)
        groupset.append(group)
    return groupset

#make a matrix of groupsets where each row of matrix is a separate possible weeks worth of groups to choose from.
def matrixgrpsets(matrix):
    list1=list(map(str,list(range(20))))
    matrix=combinelistwithself(list1,list1)    
    numiter=int(len(matrix))-1
    allgrpsets=[]
    prvgrps=[]
    for n in range(numiter):
        list1=list(map(str,list(range(20))))
        matrix=combinelistwithself(list1,list1)
        grpset=makegroupset(matrix,prvgrps)
        #print(grpset)
        for n in grpset:
            prvgrps.append(n)
        allgrpsets.append(grpset)
    return allgrpsets

#make a matrix of groupsets
list1=list(map(str,list(range(20))))
matrix=combinelistwithself(list1,list1)
matrix2=combinelistwithself(list1,list1)
#for n in matrix:
    #print(n)
    
weeks11=[[['3', '11'], ['8', '10'], ['2', '7'], ['4', '6'], ['0', '1'], ['5', '9']], [['9', '10'], ['1', '3'], ['0', '8'], ['2', '6'], ['5', '7'], ['4', '11']], [['2', '3'], ['1', '5'], ['10', '11'], ['0', '6'], ['7', '8'], ['4', '9']], [['8', '9'], ['4', '7'], ['2', '5'], ['0', '11'], ['1', '10'], ['3', '6']], [['2', '10'], ['7', '9'], ['3', '5'], ['1', '6'], ['8', '11'], ['0', '4']], [['0', '5'], ['9', '11'], ['6', '7'], ['1', '2'], ['4', '10'], ['3', '8']], [['3', '7'], ['2', '11'], ['0', '10'], ['6', '9'], ['5', '8'], ['1', '4']], [['2', '8'], ['1', '9'], ['3', '4'], ['0', '7'], ['6', '11'], ['5', '10']], [['4', '5'], ['6', '8'], ['0', '3'], ['2', '9'], ['7', '10'], ['1', '11']], [['3', '10'], ['5', '6'], ['2', '4'], ['7', '11'], ['0', '9'], ['1', '8']], [['4', '8'], ['1', '7'], ['6', '10'], ['0', '2'], ['3', '9'], ['5', '11']]]
for n in range(5):
    #print(len(weeks11))
    #for n in weeks11:
        #print(n)
    
    #prvgrps=[]
    numtries=0
    allgrpsets=[]
    
    while len(allgrpsets)<11:
        try:
            allgrpsets=matrixgrpsets(matrix)
        except:
            numtries+=1
            continue
        
    print(len(allgrpsets))
    for n in allgrpsets:
        print(n)
    input('continue?')
#print([pair[1],pair[0]])
#mat1=removerowandcolumn(matrix,pair)
#mat2=removegroup(matrix2,pair)
#for n in mat1:
    #print(n)
#for n in mat2:
    #print(n)