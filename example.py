##########################################
#                                        #
#    Example of animation with Canvas    #
#                                        #
##########################################

# We use a recursive function to repeatedly tell an object to move by some component

from Tkinter import *
root = Tk()
# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='brown')
drawpad.grid(row=0, column=0)

# Create the oval
oval = drawpad.create_oval(10, 50, 100, 100, fill='green')

# Create our animation function
def animate():
    #Move our oval object by 1 in the x direction, 0 in the y direction
    drawpad.move(oval,1,0)
    # Wait for 1 millisecond, then recursively call our animate function
    drawpad.after(1, animate)

# Kick off our animation
animate()
root.mainloop()
