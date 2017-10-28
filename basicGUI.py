import sys
from tkinter import *
from main import givenLengths, givenPoints


#Function called when button pressed
def enterValuesLength():
    #Get triangle type from givenLengths in main.py
    finalAnswerLength = givenLengths(getSide1.get(), getSide2.get(), getSide3.get())
    print(finalAnswerLength)

    #Add triangle type as a new label in GUI
    mLabel = Label(mGUI, text = finalAnswerLength).pack()

def enterValuesPoints():
    #Get triangle type from givenLengths in main.py
    finalAnswerPoints = givenPoints(getx1.get(), gety1.get(), getx2.get(), gety2.get(), getx3.get(), gety3.get())
    print(finalAnswerPoints)

    #Add lengths and triangle type as new labels in GUI
    mLabel = Label(mGUI, text = "Side 1: " + str(finalAnswerPoints[0])).pack()
    mLabel = Label(mGUI, text = "Side 2: " + str(finalAnswerPoints[1])).pack()
    mLabel = Label(mGUI, text = "Side 3: " + str(finalAnswerPoints[2])).pack()
    mLabel = Label(mGUI, text = "Type: " + str(finalAnswerPoints[3])).pack()


def lengthInput():
    #Labels/input fields for GUI (side lengths)
    mLabel = Label(mGUI, text = "Side 1").pack()
    mEntry = Entry(mGUI, textvariable = getSide1).pack()

    mLabel = Label(mGUI, text = "Side 2").pack()
    mEntry = Entry(mGUI, textvariable = getSide2).pack()

    mLabel = Label(mGUI, text = "Side 3").pack()
    mEntry = Entry(mGUI, textvariable = getSide3).pack()

    #Submit button in GUI (side lengths)
    mButton = Button(mGUI, text = "Submit Values", command = enterValuesLength, fg = "white", bg = "black").pack()

def pointInput():
    #Labels/input fields for GUI (points given)
    mLabel = Label(mGUI, text = "x1").pack()
    mEntry = Entry(mGUI, textvariable = getx1).pack()

    mLabel = Label(mGUI, text = "y1").pack()
    mEntry = Entry(mGUI, textvariable = gety1).pack()

    mLabel = Label(mGUI, text = "x2").pack()
    mEntry = Entry(mGUI, textvariable = getx2).pack()

    mLabel = Label(mGUI, text = "y2").pack()
    mEntry = Entry(mGUI, textvariable = gety2).pack()

    mLabel = Label(mGUI, text = "x3").pack()
    mEntry = Entry(mGUI, textvariable = getx3).pack()

    mLabel = Label(mGUI, text = "y3").pack()
    mEntry = Entry(mGUI, textvariable = gety3).pack()


    #Submit button in GUI (points given)
    mButton = Button(mGUI, text = "Submit Values", command = enterValuesPoints, fg = "white", bg = "black").pack()



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
mGUI.geometry("600x600")
mGUI.title("Triangle Calculator")
mGUI.mainloop()
