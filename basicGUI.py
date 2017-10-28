import sys
from tkinter import *


#Function called when button pressed
def enterValues():
    print("VALUES: " + str(getHypotenuse.get()) + " " + str(getSideX.get()) + " " + str(getSideY.get()))
    givenLengths(getHypotenuse.get(), getSideX.get(), getSideY.get())



#Setting up GUI and variables for input
mGUI = Tk()
getHypotenuse = IntVar()
getSideX = IntVar()
getSideY = IntVar()
mGUI.geometry("600x600")
mGUI.title("Triangle Calculator")

#Labels/input fields for GUI
mLabel = Label(mGUI, text = "Hypotenuse").pack()
mEntry = Entry(mGUI, textvariable = getHypotenuse).pack()

mLabel = Label(mGUI, text = "SideX").pack()
mEntry = Entry(mGUI, textvariable = getSideX).pack()

mLabel = Label(mGUI, text = "SideY").pack()
mEntry = Entry(mGUI, textvariable = getSideY).pack()


#Button in GUI
mButton = Button(mGUI, text = "Submit Values", command = enterValues, fg = "white", bg = "black").pack()


#Run GUI
mGUI.mainloop()
