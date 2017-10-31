import os
import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
from trig import givenLengths, givenPoints
from C2F import C_to_F_converter, F_to_C_converter
from dictionary import dictionary
from calc import startCalc
from playsound import playsound

#Create new label with output value on specified page
def newLabel(strOut, pageNum):
    if(pageNum == page3):
        wrapNum = 500
    else:
        wrapNum = 0
    Label(pageNum, text = strOut, wraplength = wrapNum).pack()


def newLabelpg1(strOut):
    mLabel = Label(page1, text = strOut).pack()
def newLabelpg2(strOut):
    mLabel = Label(page2, text = strOut).pack()
def newLabelpg3(strOut):
    mLabel = Label(page3, text = strOut, wraplength = 500).pack()

#Function called when button pressed if lengths of sides are entered (page1)
def enterValuesLength():
    #Get triangle type from givenLengths in main.py
    finalAnswerLength = givenLengths(getSide1.get(), getSide2.get(), getSide3.get())
    print(finalAnswerLength)

    #Add triangle type as a new label in GUI
    newLabel(finalAnswerLength, page1)

#Function called when button pressed if points of triangle are entered (page1)
def enterValuesPoints():
    #Get triangle type from givenLengths in main.py
    finalAnswerPoints = givenPoints(getx1.get(), gety1.get(), getx2.get(), gety2.get(), getx3.get(), gety3.get())
    print(finalAnswerPoints)

    #Add lengths and triangle type as new labels in GUI
    newLabel("Side 1: " + str(finalAnswerPoints[0]) +
            "\nSide 2: " + str(finalAnswerPoints[1]) +
            "\nSide 3: " + str(finalAnswerPoints[2]) +
            "\nType: " + str(finalAnswerPoints[3]),
            page1)

#Creates input field/labels/buttons for length input (page1)
def lengthInput():
    #Labels/input fields for GUI (side lengths)
    newLabel("Side 1", page1)
    mEntry = Entry(page1, textvariable = getSide1).pack()

    newLabel("Side 2", page1)
    mEntry = Entry(page1, textvariable = getSide2).pack()

    newLabel("Side 3", page1)
    mEntry = Entry(page1, textvariable = getSide3).pack()

    #Submit button in GUI (side lengths)
    mButton = Button(page1, text = "Submit Lengths", command = enterValuesLength, fg = "white", bg = "black").pack()

#Creates input field/labels/buttons for point input (page1)
def pointInput():
    #Labels/input fields for GUI (points given)
    newLabel("x1", page1)
    mEntry = Entry(page1, textvariable = getx1).pack()

    newLabel("y1", page1)
    mEntry = Entry(page1, textvariable = gety1).pack()

    newLabel("x2", page1)
    mEntry = Entry(page1, textvariable = getx2).pack()

    newLabel("y2", page1)
    mEntry = Entry(page1, textvariable = gety2).pack()

    newLabel("x3", page1)
    mEntry = Entry(page1, textvariable = getx3).pack()

    newLabel("y3", page1)
    mEntry = Entry(page1, textvariable = gety3).pack()


    #Submit button in GUI (points given)
    mButton = Button(page1, text = "Submit Points", command = enterValuesPoints, fg = "white", bg = "black").pack()


#Function called when button pressed if °C entered (page2)
def enterC():
    finalF = C_to_F_converter(getC.get())
    print(finalF)
    newLabel(str(getC.get()) + "°C = " + str(finalF) + "°F", page2)

#Function called when button pressed if °F entered (page2)
def enterF():
    finalC = F_to_C_converter(getF.get())
    print(finalC)
    newLabel(str(getF.get()) + "°F = " + str(finalC) + "°C", page2)

#Creates input field/labels/buttons for °C input (page2)
def cDegreeInput():
    newLabel("Convert °C to °F", page2)
    mEntry = Entry(page2, textvariable = getC).pack()
    mButton = Button(page2, text = "Submit °C Value", command = enterC, fg = "white", bg = "black").pack()

#Creates input field/labels/buttons for °F input (page2)
def fDegreeInput():
    newLabel("Convert °F to °C", page2)
    mEntry = Entry(page2, textvariable = getF).pack()
    mButton = Button(page2, text = "Submit °F Value", command = enterF, fg = "white", bg = "black").pack()

#Function called when button pressed to enter word (page3)
def enterWord():
    wordDef = ((str(dictionary(getWord.get())).strip('[]'))).strip("''")
    if(wordDef == "Not found in dictionary."):
        newLabel(wordDef, page3)
    elif(wordDef == "YOU FEELING THE MEMES HASSAN!!"):
        print("CYRUS AUDIO")
        newLabel(getWord.get() + " = " + wordDef, page3)
        playsound('memes.mp3')
        print("AUDIO DONE")
    else:
        newLabel(getWord.get() + " = " + wordDef, page3)
    print(wordDef)
    print(getWord.get())

#Creates input field/labels/buttons for word input (page3)
def wordInput():
    newLabel("Word: ", page3)
    mEntry = Entry(page3, textvariable = getWord).pack()
    mButton = Button(page3, text = "Submit Word", command = enterWord, fg = "white", bg = "black").pack()


#Works good enough
def mainCalc():
    mButton = Button(page4, text = "Open calculator", command = startCalc, fg = "white", bg = "green").pack()
def cal():
    os.system("calc.py")

#``````````````````````````````````````````````````````````````````````````````````````````````````````````````````
#``             '''DO not do anything past this line if you are not samrt'''                                     ``
#``````````````````````````````````````````````````````````````````````````````````````````````````````````````````

#Setting up GUI (and tabs) and variables for input
mGUI = Tk()
nb = ttk.Notebook(mGUI)
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
page3 = ttk.Frame(nb)
page4 = ttk.Frame(nb)
nb.add(page1, text = "Triangle Calculator")
nb.add(page2, text = "Degree Converter")
nb.add(page3, text = "Dictionary")
nb.add(page4, text = "Calculator")
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
mainCalc()

#Run/setup GUI
mGUI.geometry("600x900")
mGUI.title("A bunch of things that seem useful")
mGUI.mainloop()
