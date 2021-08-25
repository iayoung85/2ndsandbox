# Loads an image and then converts it to a negative image

# Import the cImage module, but call it 'image' to be the same as in the book
import cImage as image

# Loads an image.  The named file needs to be in the same directory as
# this python file.  Note we can only process .gif images with cImage.
img = image.Image("cy.gif")

# Creates a window on which to display the image
# Note that unlike in the book, we have to provide three arguments.
# The firet argument is the title for the window, then the width and height.
win = image.ImageWin("cy", img.getWidth(), img.getHeight())

# Draws the image on the window
img.draw(win)

# Iterate over the rows and columns
for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        
        # get a pixel
        p = img.getPixel(col, row)

        # compute new red, green, and blue values
        newred = 255 - p.getRed()
        newgreen = 255 - p.getGreen()
        newblue = 255 - p.getBlue()
        
        # create a new pixel from the new color values
        newpixel = image.Pixel(newred, newgreen, newblue)
        
        # set the new pixel at the same row and column
        # Note that the column comes first!
        img.setPixel(col, row, newpixel)

    # redraw the image after processing one row.
    # COMMENT OUT this line to speed things up!
    img.draw(win)
    
# When we're all done, be sure to draw the image
img.draw(win)

# Optionally, save the new image into a new file
# UNCOMMENT this line to save the image.
# WARNING: if you already have a file with this name, it will be destroyed!
#img.saveTk("NegativeImage.gif")

# Exit when window is clicked
win.exitonclick()