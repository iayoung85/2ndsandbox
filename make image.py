# Creates an empty image and then fills in some pixels
# to draw a gradient that transitions from red to green.

import cImage as image

# A width and height for the new image
width = 500
height = 500

# Create an "empty" image of the given size.
# Notice we have to specify the width and height.
img = image.EmptyImage(width, height)

# Create a window
win = image.ImageWin("test", width, height)

def isred(p):
    r=p.getRed()
    g=p.getGreen()
    b=p.getBlue()
    if r==255 and g==0 and b==0:
        return True
    else:
        return False
def isblue(p):
    r=p.getRed()
    g=p.getGreen()
    b=p.getBlue()
    if r==0 and g==0 and b==255:
        return True
    else:
        return False

# Iterate over pixels
for row in range(height-1):
    for col in range(width-1):
        if row==0 or col==0:
            p1=img.getPixel(col,row)
            p1.setRed(255)
            p1.setBlue(0)
            p1.setGreen(0)
            img.setPixel(col,row,p1)
        else:
            p=img.getPixel(col,row)
            pleft=img.getPixel(col-1,row)
            pdiag=img.getPixel(col-1,row-1)
            pabove=img.getPixel(col,row-1)
            startingsum=0
            if isred(pleft)==True:
                startingsum+=1
            elif isblue(pleft)==True:
                startingsum+=2
            if isred(pdiag)==True:
                startingsum+=1
            elif isblue(pdiag)==True:
                startingsum+=2
            if isred(pabove)==True:
                startingsum+=1
            elif isblue(pabove)==True:
                startingsum+=2
            startingsum=startingsum%3
            if startingsum==1:
                p.setRed(255)
                p.setBlue(0)
                p.setGreen(0)
                img.setPixel(col,row,p)
            elif startingsum==2:
                p.setRed(0)
                p.setBlue(255)
                p.setGreen(0)
                img.setPixel(col,row,p)
            else:
                p.setRed(255)
                p.setBlue(255)
                p.setGreen(255)
                img.setPixel(col,row,p)
    # comment this line to speed things up
        #img.draw(win)        

img.draw(win)

# uncomment this to save the image as a file
#img.saveTk("gradient.gif")

win.exitonclick()
