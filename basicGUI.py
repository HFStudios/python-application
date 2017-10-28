import sys
from tkinter import *
from Trig import givenLengths, givenPoints


#Create new label with output value
def newLabel(strOut):
    mLabel = Label(mGUI, text = strOut).pack()

#Function called when button pressed
def enterValuesLength():
    #Get triangle type from givenLengths in main.py
    finalAnswerLength = givenLengths(getSide1.get(), getSide2.get(), getSide3.get())
    print(finalAnswerLength)

    #Add triangle type as a new label in GUI
    newLabel(finalAnswerLength)

def enterValuesPoints():
    #Get triangle type from givenLengths in main.py
    finalAnswerPoints = givenPoints(getx1.get(), gety1.get(), getx2.get(), gety2.get(), getx3.get(), gety3.get())
    print(finalAnswerPoints)

    #Add lengths and triangle type as new labels in GUI
    newLabel("Side 1: " + str(finalAnswerPoints[0]) +
            "\nSide 2: " + str(finalAnswerPoints[1]) +
            "\nSide 3: " + str(finalAnswerPoints[2]) +
            "\nType: " + str(finalAnswerPoints[3]))


def lengthInput():
    #Labels/input fields for GUI (side lengths)
    newLabel("Side 1")
    mEntry = Entry(mGUI, textvariable = getSide1).pack()

    newLabel("Side 2")
    mEntry = Entry(mGUI, textvariable = getSide2).pack()

    newLabel("Side 3")
    mEntry = Entry(mGUI, textvariable = getSide3).pack()

    #Submit button in GUI (side lengths)
    mButton = Button(mGUI, text = "Submit Lengths", command = enterValuesLength, fg = "white", bg = "black").pack()

def pointInput():
    #Labels/input fields for GUI (points given)
    newLabel("x1")
    mEntry = Entry(mGUI, textvariable = getx1).pack()

    newLabel("y1")
    mEntry = Entry(mGUI, textvariable = gety1).pack()

    newLabel("x2")
    mEntry = Entry(mGUI, textvariable = getx2).pack()

    newLabel("y2")
    mEntry = Entry(mGUI, textvariable = gety2).pack()

    newLabel("x3")
    mEntry = Entry(mGUI, textvariable = getx3).pack()

    newLabel("y3")
    mEntry = Entry(mGUI, textvariable = gety3).pack()


    #Submit button in GUI (points given)
    mButton = Button(mGUI, text = "Submit Points", command = enterValuesPoints, fg = "white", bg = "black").pack()



#Setting up GUI and variables for input
mGUI = Tk()

#Values if given lengths
getSide1 = IntVar()
getSide2 = IntVar()
getSide3 = IntVar()

#Values if given points
getx1 = IntVar()
gety1 = IntVar()
getx2 = IntVar()
gety2 = IntVar()
getx3 = IntVar()
gety3 = IntVar()


lengthInput()
pointInput()


#Run/setup GUI
mGUI.geometry("300x900")
mGUI.title("Triangle Calculator")
mGUI.mainloop()
