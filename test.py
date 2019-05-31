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






if __name__ == "__main__":
    main3()
