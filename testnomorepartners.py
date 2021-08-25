def nomorepartners(studentname,allprevpairs,attendance):
    print(attendance)
    print("the student's name is " +studentname)
    studentsprevpartners=[]
    for n in allprevpairs:
        
        if studentname in n:
            print(n)
            for i in n:
                
                if i!=studentname:
                    print(i)
                    studentsprevpartners.append(i)
    print(studentsprevpartners)
    for n in attendance:
        if n not in studentsprevpartners and n!=studentname:
            return False
    return 'true'
testcase=nomorepartners('test1', [['test5', 'test4'], ['join another group', 'test2'], ['test1', 'test3'], ['test2', 'test5'], ['test1', 'test4'], ['test3', 'join another group'], ['test4', 'join another group'], ['test1', 'test5'], ['test2', 'test3'], ['test3', 'test4'], ['join another group', 'test5'], ['test1', 'test2'], ['test1', 'join another group'], ['test5', 'test3'], ['test4', 'test2']],['test1', 'test2', 'test3', 'test4', 'test5', 'join another group'])
print(testcase)