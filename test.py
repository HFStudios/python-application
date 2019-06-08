import json
from subprocess import call


data = json.load(open("data.json"))


def main():
    f = open("words.txt","w+")
    for i in data:
        f.write(i+"\n")
    f.close()

def main2():
    f = open("simpleWords.txt","w+")
    oldF = open("words.txt","r")

    for i in oldF:
        for w in i.split():
            f.write(w+"\n")


def main3():
    seen = set()
    with open("simpleWords.txt","r") as old:
        with open("parse2.txt","w+") as new:
            for word in old:
                if word not in seen:
                    seen.add(word)
                    #str.format("{}\n", word)
                    new.write(f"{word}")



def main4():
    old = open("parse2.txt", "r")
    new = open("3to8Len.txt", "w+")

    for words in old:
        if(len(words.rstrip("\n")) >= 3 and len(words.rstrip("\n")) <= 8):
            new.write(words)

def removeNum():
    read = open("3to8Len.txt", "r")
    new = open("noNum.txt", "w+")

    for word in read:
        if( not any(char.isdigit() for char in word)):
            new.write(word)
    
def main5():
    read = open("noNum.txt", "r")
    new = open("lowerCase.txt", "w+")
    new2 = open("noNum-lowerCase.txt", "w+")

    for word in read:
        new.write(word.lower())

    read.close()
    new.close()
    new2.close()
    
    print("part one done")
    
    seen = set()
    with open("lowerCase.txt","r") as old:
        with open("noNum-lowerCase.txt","w+") as new:
            for word in old:
                if word not in seen:
                    seen.add(word)
                    #str.format("{}\n", word)
                    new.write(f"{word}")

def rmWeirdThing():
    read = open("noNum-lowerCase.txt", "r")
    new = open("final-v1.txt", "w+")

    for word in read:
        bad = {"-", ",","'","*"}
        badB = False
        for char in word:
            if(char in bad):
                badB = True

        if(not badB):
            new.write(word)
def onlyEng():
    read = open("final-v1.txt", "r")
    new = open("final-v2.txt", "w+")

    eng = {"\n","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
    for word in read:
        badW = False
        for char in word:
            if(char not in eng):
                badW = True
        if(not badW):
            new.write(word)

def wordLength():
    read = open("final-v2.txt", "r")

    for i in range(3,9):
        tempF = open("final-Len"+str(i)+".txt", "w+")

        for words in read:
            
            if(len(words.rstrip("\n")) == i):
               tempF.write(words)
        
        tempF.close()

if __name__ == "__main__":
    wordLength()
