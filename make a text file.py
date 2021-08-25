#f= open("guru99.txt","w+")
#f.write("this is a test of your testing center")
#f.close()

file= open("guru99.txt","r")
test=file.read()
print(test)
file.close()

file=open("guru99.txt","a")
file.write("does this create a second line in the text file?")
file.write("does this create a 3rd line in the text file?")
file.write("and a 4th?")
file.close()
file=open("guru99.txt","r")
line=file.read()
for line in file:
    
    print(line)
file.close()