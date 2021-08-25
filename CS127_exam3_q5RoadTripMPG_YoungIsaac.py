class FillUp:
 def __init__(self, gals, miles):
  self.gallons = gals
  self.miles = miles

 def get_gallons(self):
  return self.gallons

 def get_miles(self):
  return self.miles
 def compute_mpg(self):
  return self.miles / self.gallons
 def read_mileage_file(self,nexttrip):
  galstot=self.gallons+nexttrip.gallons
  milestot=nexttrip.miles+self.miles
  return FillUp(galstot,milestot)

filein=open('MileGallons.csv','r')

firstline=filein.readline()
linelist=firstline.split(', ')
print(linelist)
linelist[1]=(linelist[1][:-1])
print(linelist)
initialmiles=int(linelist[1])
print(initialmiles)
cartrip=FillUp(0,0)
for newline in filein:
 print(newline)
 listnewline=newline.split(', ')
 listnewline[0]=float(listnewline[0])
 listnewline[1]=int(listnewline[1])
 print(listnewline)
 currentfillup=FillUp(listnewline[0],listnewline[1]-initialmiles)
 cartrip=cartrip.read_mileage_file(currentfillup)
 initialmiles=listnewline[1]
print(cartrip.compute_mpg())
print(cartrip.get_miles())
print(cartrip.get_gallons())
filein.close()