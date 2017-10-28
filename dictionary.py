import json

data = json.load(open("data.json"))

def dic(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        print("Not a word!")

word = input("What word do you want to know about?")

print(dic(word))
