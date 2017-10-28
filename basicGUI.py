import sys
from tkinter import *
from main import givenLengths


#Function called when button pressed
def enterValues():
    #Get triangle type from givenLengths in main.py
    finalAnswer = givenLengths(getHypotenuse.get(), getSideX.get(), getSideY.get())
    print(finalAnswer)

    #Add triangle type as a new label in GUI
    mLabel = Label(mGUI, text = finalAnswer).pack()



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



#Submit button in GUI
mButton = Button(mGUI, text = "Submit Values", command = enterValues, fg = "white", bg = "black").pack()


#Run GUI
mGUI.mainloop()
