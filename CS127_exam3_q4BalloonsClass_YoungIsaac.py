class Balloon:
    """The balloon class is for representing and manipulating a toy called a baloon which holds air"""
    def __init__(self,maxrad):
        """ create a new deflated balloon radius 0 with no air inside with a user defined maximum radius where it will pop if more air is added"""
        self.maximumradius=maxrad
        self.radius=0
        self.popped=False
    def blow(self,rad):
        self.radius+=rad
        if self.radius>self.maximumradius:
            self.popped=True
        if self.popped==True:
            self.radius=0
        return self
    def get_radius(self):
        return self.radius
    def deflate(self):
        self.radius=0
        return self
    
test=Balloon(5)
print(test.get_radius())

test.deflate()
print(test.get_radius())

test.blow(4)
print(test.get_radius())

test.blow(2)
print(test.get_radius())

test.blow(1)
print(test.get_radius())

b2=Balloon(4)
b2.blow(4)
print(b2.get_radius())