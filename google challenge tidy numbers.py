#given integer, determines if it digits are ordered such that all of the digits are in a non-decreasing order. 
def checker(i):
    stri=str(i)
    for n in range(len(stri)-1):
        if int(stri[n])>int(stri[n+1]):
            return False
    return True
def reducer(i):
    stri=str(i)
    #print(stri)
    for n in range(len(stri)):
        if int(stri[n])>int(stri[n+1]):
            #print(stri[:n])
            stri=str(stri[:n])+str(int(stri[n])-1)+'9'*len(stri[n+1:])
            return stri
def program(i):
    while checker(i)==False:
        i=reducer(i)
    stri=str(i)
    if stri[0]=='0'and len(stri)>1:
        stri=stri[1:]
        return int(stri)
    return i
filein=open('B-large-practice.in','r')
T=filein.readline()
allnumbers=[]
for line in filein:
    allnumbers.append(line[:-1])
filein.close()
outfile=open('googleprettynumberslarge.out','w')
for n in range(len(allnumbers)):
    newnumber=program(allnumbers[n])
    print(newnumber)
    outfile.write('Case #'+ str(n+1)+': '+str(newnumber)+'\n')
outfile.close()