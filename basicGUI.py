import sys
from tkinter import *
from tkinter import ttk
from Trig import givenLengths, givenPoints
from C2F import C_to_F_converter, F_to_C_converter
from dictionary import dictionary


#Create new label with output value
def newLabelpg1(strOut):
    mLabel = Label(page1, text = strOut).pack()
def newLabelpg2(strOut):
    mLabel = Label(page2, text = strOut).pack()
def newLabelpg3(strOut):
    mLabel = Label(page3, text = strOut).pack()

#Function called when button pressed
def enterValuesLength():
    #Get triangle type from givenLengths in main.py
    finalAnswerLength = givenLengths(getSide1.get(), getSide2.get(), getSide3.get())
    print(finalAnswerLength)

    #Add triangle type as a new label in GUI
    newLabelpg1(finalAnswerLength)

def enterValuesPoints():
    #Get triangle type from givenLengths in main.py
    finalAnswerPoints = givenPoints(getx1.get(), gety1.get(), getx2.get(), gety2.get(), getx3.get(), gety3.get())
    print(finalAnswerPoints)

    #Add lengths and triangle type as new labels in GUI
    newLabelpg1("Side 1: " + str(finalAnswerPoints[0]) +
            "\nSide 2: " + str(finalAnswerPoints[1]) +
            "\nSide 3: " + str(finalAnswerPoints[2]) +
            "\nType: " + str(finalAnswerPoints[3]))

def lengthInput():
    #Labels/input fields for GUI (side lengths)
    newLabelpg1("Side 1")
    mEntry = Entry(page1, textvariable = getSide1).pack()

    newLabelpg1("Side 2")
    mEntry = Entry(page1, textvariable = getSide2).pack()

    newLabelpg1("Side 3")
    mEntry = Entry(page1, textvariable = getSide3).pack()

    #Submit button in GUI (side lengths)
    mButton = Button(page1, text = "Submit Lengths", command = enterValuesLength, fg = "white", bg = "black").pack()

def pointInput():
    #Labels/input fields for GUI (points given)
    newLabelpg1("x1")
    mEntry = Entry(page1, textvariable = getx1).pack()

    newLabelpg1("y1")
    mEntry = Entry(page1, textvariable = gety1).pack()

    newLabelpg1("x2")
    mEntry = Entry(page1, textvariable = getx2).pack()

    newLabelpg1("y2")
    mEntry = Entry(page1, textvariable = gety2).pack()

    newLabelpg1("x3")
    mEntry = Entry(page1, textvariable = getx3).pack()

    newLabelpg1("y3")
    mEntry = Entry(page1, textvariable = gety3).pack()


    #Submit button in GUI (points given)
    mButton = Button(page1, text = "Submit Points", command = enterValuesPoints, fg = "white", bg = "black").pack()



def enterC():
    finalF = C_to_F_converter(getC.get())
    print(finalF)
    newLabelpg2(str(getC.get()) + "°C = " + str(finalF) + "°F")

def enterF():
    finalC = F_to_C_converter(getF.get())
    print(finalC)
    newLabelpg2(str(getF.get()) + "°F = " + str(finalC) + "°C")

def cDegreeInput():
    newLabelpg2("Convert °C to °F")
    mEntry = Entry(page2, textvariable = getC).pack()
    mButton = Button(page2, text = "Submit °C Value", command = enterC, fg = "white", bg = "black").pack()

def fDegreeInput():
    newLabelpg2("Convert °F to °C")
    mEntry = Entry(page2, textvariable = getF).pack()
    mButton = Button(page2, text = "Submit °F Value", command = enterF, fg = "white", bg = "black").pack()


def enterWord():
    wordDef = (str(dictionary(getWord.get())).strip('[]'))
    newLabelpg3(getWord.get() + " = " + wordDef)
    print(wordDef)
    print(getWord.get())

def wordInput():
    newLabelpg3("Word: ")
    mEntry = Entry(page3, textvariable = getWord).pack()
    mButton = Button(page3, text = "Submit Word", command = enterWord, fg = "white", bg = "black").pack()




#Setting up GUI (and tabs) and variables for input
mGUI = Tk()
nb = ttk.Notebook(mGUI)
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
page3 = ttk.Frame(nb)
nb.add(page1, text = "Triangle Calculator")
nb.add(page2, text = "Degree Converter")
nb.add(page3, text = "Dictionary")
nb.pack(expand = 1, fill = "both")


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

#Values for degree conversion
getC = IntVar()
getF = IntVar()

#Values for Dictionary
getWord = StringVar()


#Run functions to display in window
lengthInput()
pointInput()
cDegreeInput()
fDegreeInput()
wordInput()


#Run/setup GUI
mGUI.geometry("600x900")
mGUI.title("Triangle Calculator")
mGUI.mainloop()
