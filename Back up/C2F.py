
#Converts  celsius to fahrenheit
def C_to_F_converter(C):
    F = (C * (9 / 5)) + 32
    return F

#Converts fahrenheit to celsius
def F_to_C_converter(F):
    C = (F - 32) * (5 / 9)
    return C

#Runs terminal version of program
def main():
    while True:
        getInput = input("Convert celsius to fahrenheit (1) or fahrenheit to celsius (2)? ")
        if(getInput == "1"):
            wanted = 1
            break
        elif(getInput == "2"):
            wanted = 2
            break
        else:
            print("Choose a real selection: ")
    if(wanted == 1):
        C = float(input("What is the number of degrees celsius to convert to fahrenheit? "))
        print(str(C) + "°C = " + str(C_to_F_converter(C)) + "°F")
    elif(wanted == 2):
        F = float(input("What is the number of degrees fahrenheit to convert to celsius? "))
        print(str(F) + "°F = " + str(F_to_C_converter(F)) + "°C")


#If file is run as standalone, run main() function
if __name__ == "__main__":
    main()
