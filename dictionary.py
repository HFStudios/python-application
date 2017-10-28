import json

data = json.load(open("data.json"))

#Looks for word in data.json file (dictionary file)
def dictionary(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return("That word is not in the dictionary.")

#Runs terminal version of program
def main():
    wIn = input("What word do you want to know about?")
    print(str(dictionary(wIn)))


#If file is run as standalone, run main() function
if __name__ == "__main__":
    main()
