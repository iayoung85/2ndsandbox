testlist=['a','b','c','d','a']
print(testlist)
abtestlist=[]
for n in range(len(testlist)):
    print(testlist[n])
    if testlist[n]!='a':
        abtestlist.append(testlist[n])
print(abtestlist)