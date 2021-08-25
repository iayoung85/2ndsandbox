##for n in range(5,1,-1):
    
    ##print(n,'bottles of beer on the wall!')
    ##print(n,'bottles of beer!')
    ##print('Take one down!')
    ##print('Pass it around!')
    ##print(n-1,'bottles of beer on the wall!')
    ##print()
#sumtot=100/0.9
#for n in range(10):
    #sumtot=0.9*sumtot
    #print(sumtot)
    
import tkinter as tki

class Application(tki.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tki.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tki.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tki.Tk()
app = Application(master=root)
app.mainloop()