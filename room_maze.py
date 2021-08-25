class Person:
    initialdoorstate = "0000000000000000"
    def __init__(self,position):
        self.doorstate = "0000000000000000"
        self.position=position
    def checklegaldoor(self,position,doornumber):
        if doornumber == 1 or doornumber ==3:
            if position ==1 or position == 6:
                return True
        elif doornumber == 10 or doornumber ==14:
            if position ==3 or position == 6:
                return True
        elif doornumber == 16 or doornumber ==13:
            if position ==5 or position == 6:
                return True
        elif doornumber == 2 or doornumber ==5:
            if position ==2 or position == 6:
                return True
        elif doornumber == 4:
            if position ==1 or position == 2:
                return True
        elif doornumber == 6:
            if position ==1 or position == 3:
                return True
        elif doornumber == 7:
            if position ==1 or position == 4:
                return True
        elif doornumber == 8:
            if position ==4 or position == 2:
                return True
        elif doornumber == 9:
            if position ==5 or position == 2:
                return True
        elif doornumber == 11:
            if position ==3 or position == 4:
                return True
        elif doornumber == 12:
            if position ==4 or position == 5:
                return True
        elif doornumber == 15:
            if position ==4 or position == 6:
                return True        
        else: 
            return False
    def switchrooms(self,position,doornumber):
        if doornumber == 1 or doornumber ==3:
            if position ==1:
                self.position=6
            elif position == 6:
                self.position=1
        elif doornumber == 10 or doornumber ==14:
            if position ==3:
                self.position=6
            elif position == 6:
                self.position=3
        elif doornumber == 16 or doornumber ==13:
            if position ==5: 
                self.position=6
            elif position == 6:
                self.position=5
        elif doornumber == 2 or doornumber ==5:
            if position ==2:
                self.position=6
            elif position == 6:
                self.position=2
        elif doornumber == 4:
            if position ==1:
                self.position=2
            elif position == 2:
                self.position=1
        elif doornumber == 6:
            if position ==1:
                self.position=3
            elif position == 3:
                self.position=1
        elif doornumber == 7:
            if position ==1:
                self.position=4
            elif position == 4:
                self.position=1
        elif doornumber == 8:
            if position ==4:
                self.position=2
            elif position == 2:
                self.position=4
        elif doornumber == 9:
            if position ==5:
                self.position=2
            elif position == 2:
                self.position=5
        elif doornumber == 11:
            if position ==3:
                self.position=4
            elif position == 4:
                self.position=3
        elif doornumber == 12:
            if position ==4:
                self.position=5
            elif position == 5:
                self.position=4
        elif doornumber == 15:
            if position ==4:
                self.position=6
            elif position == 6:
                self.position=4
        else:
            print("something went wrong in switchrooms")
    def passthroughdoor(self,position,doornumber):
        if self.checklegaldoor(position,doornumber)==True:
            if self.doorstate[doornumber-1]=="0":
                predoors=self.doorstate[:doornumber-1]
                afterdoors=self.doorstate[doornumber:]
                self.doorstate=predoors+"1"+afterdoors
                self.switchrooms(position,doornumber)
            else:
                print("illegal door passthrough")
                return False
        else:
            print("illegal door passthrough")
            return False
#adds new line to an existing textfile    
def writeline(directoryfilename,string):
    outfile=open(directoryfilename,"a")
    outfile.write(string+"\n")
    outfile.close()


def listpossibilities(persona):
    if persona.position==1:
        doorpossibilities=[1,3,4,6,7]
    elif persona.position==2:
        doorpossibilities=[2,4,5,8,9]
    elif persona.position==3:
        doorpossibilities=[6,10,11,14]
    elif persona.position==4:
        doorpossibilities=[7,8,11,12,15]
    elif persona.position==5:
        doorpossibilities=[9,12,13,16]
    elif persona.position==6:
        doorpossibilities=[1,2,3,5,10,13,14,15,16]
    else:
        print("there was an error in listpossibilities")
        return "error"
    returnlist=[]
    for door in doorpossibilities:
        if persona.doorstate[door-1]=="0":
            returnlist.append(door)
    return returnlist

def endgame(persona):
    doorpossibilities=listpossibilities(persona)
    if len(doorpossibilities)==0:
        #print("the game is over")
        return False
    listtruths=[]
    for door in doorpossibilities:
        if persona.doorstate[door-1]=="1":
            listtruths.append("false")    
        else:
            listtruths.append("true")
    if "true" in listtruths:
        return True
    else:
        #print("the game is over")
        return False

#generate doorstate string go be used in order to generate an accurate list of possibilities to try

def playpartialgame(startingroom,prevdoors,currentstepdoorsusedalready):
    persona=Person(startingroom)
    for n in prevdoors:
        persona.passthroughdoor(persona.position,n)
    possibilities=listpossibilities(persona)
    for n in possibilities:
        if n not in currentstepdoorsusedalready:
            newdoortotry=n
            break
        persona.passthroughdoor(persona.position,newdoortotry)
    #print(persona.doorstate)
    return persona.doorstate

def playagame(startingroom,prevdoors,currentstepdoorsusedalready):
    persona=Person(startingroom)
    outputdoorsequence=[]
    for n in prevdoors:
        persona.passthroughdoor(persona.position,n)
        outputdoorsequence.append(n)
    possibilities=listpossibilities(persona)
    for n in possibilities:
        if n not in currentstepdoorsusedalready:
            newdoortotry=n
            break
    persona.passthroughdoor(persona.position,newdoortotry)
    outputpartialdoorstate=persona.doorstate
    #print(outputpartialdoorstate)
    outputdoorsequence.append(newdoortotry)
    while endgame(persona):
        doorpossibilities=listpossibilities(persona)
        doorchoice=doorpossibilities[0]
        outputdoorsequence.append(doorchoice)
        persona.passthroughdoor(persona.position,doorchoice)
        #print(persona.doorstate)
    #print(outputdoorsequence)
    return outputdoorsequence
def makeasubtree(startingroom,prevdoors,currentstepdoorsusedalready):
    persona=Person(startingroom)
    for n in prevdoors:
        persona.passthroughdoor(persona.position,n)
    possibilities=listpossibilities(persona)
    realpossibilities=[]
    for n in possibilities:
        if n not in currentstepdoorsusedalready:
            realpossibilities.append(n)
    masterlist=[]
    doorstried=[]
    while len(realpossibilities)>0:
        newgame=playagame(1,prevdoors,doorstried)
        masterlist.append(newgame)
        doorstried.append(newgame[len(prevdoors)])
        realpossibilities.remove(newgame[len(prevdoors)])
    return masterlist

def ultimatetree(startingroom,masterlist,stepnumber):
    listofbeginnings=[]
    for n in masterlist:
        if type(n) == int:
            if n not in listofbeginnings:
                listofbeginnings.append(n)
        elif n[:stepnumber] not in listofbeginnings:
            listofbeginnings.append(n[:stepnumber])
    print("there were " + str(len(listofbeginnings))+ " "+str(stepnumber)+"mer beginning combinations")
    for n in listofbeginnings:
        persona=makeasubtree(1,n,[])
        for n in persona:
            masterlist.append(n)
    print("there were " + str(len(masterlist))+" attempts made to get to a completed maze")
    print ("the longest we made it to was " + str(len(max(masterlist,key=len))) + " steps")
    print ("the best sequence we found was " +str(max(masterlist,key=len)))
    return masterlist

masterlist=[]
persona=makeasubtree(1,[],[])
for n in persona:
    masterlist.append(n)

for n in range(14):
    ultimatetree(1,masterlist,n)

#newlist=[]
#for n in persona:
    #if n[:1] not in newlist:
        #newlist.append(n[:1])
#print("there were " + str(len(newlist))+ " onemer combinations")
#for n in newlist:
    #secondpersona=makeasubtree(1,[n],[])
    #for n in secondpersona:
        #masterlist.append(n)
#print(len(masterlist))
#print (len(max(masterlist,key=len)))

#newlist_twomers=[]
#for n in masterlist:
    #if n[:2] not in newlist_twomers:
        #newlist_twomers.append(n[:2])
#print("there were " + str(len(newlist_twomers))+ " twomer combinations")
#for n in newlist_twomers:
    #thirdpersona=makeasubtree(1,n,[])
    #for n in thirdpersona:
        #masterlist.append(n)
#print("there were " + str(len(masterlist))+" attempts made to get to a completed maze")
#print ("the longest we made it to was " + str(len(max(masterlist,key=len))) + " steps")
#print ("the best sequence we found was " +str(max(masterlist,key=len)))

#persona.passthroughdoor(persona.position,1)
#print(persona.doorstate)
#print(persona.position)
#persona.passthroughdoor(persona.position,1)
#print(persona.doorstate)
#print(persona.position)

#trynumber=1
#save_path="D:\\Box Sync\\Documents\\python coding folder\\room_maze_problem\\listed attempts"
#samplename="attempts"+str(trynumber)+".txt"
#completename=save_path+"\\"+samplename
#print(completename)
#outfile=open(completename,"w")
#outfile.write(str(date.today())+"\n")
#outfile.close()