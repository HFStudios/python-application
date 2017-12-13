C = 0
K = 0
#Converts  celsius to fahrenheit
def C_to_F_converter(C):
    F = (C * (9 / 5)) + 32
    return F

#Converts fahrenheit to celsius
def F_to_C_converter(F):
    C = (F - 32) * (5 / 9)
    return C
#Converts Kelvin to celsius
def k_to_c_converter(C):
    K = C - 273.15
    return K
#Converts celsius to Kelvin
def c_to_k_converter(K):
    C = K + 273.15
    return C

#Runs terminal version of program
def main():
    while True:
        getInput = input("Convert celsius to fahrenheit (1) or fahrenheit to celsius (2) or kelvin to celsius? ")
        if(getInput == "1"):
            wanted = 1
            break
        elif(getInput == "2"):
            wanted = 2
            break
        elif(getInput == "3"):
            wanted = 3
            break
        elif(getInput == "4"):
            wanted = 4
        else:
            print("Choose a real selection: ")
    if(wanted == 1):
        C = float(input("What is the number of degrees celsius to convert to fahrenheit? "))
        print(str(C) + "°C = " + str(C_to_F_converter(C)) + "°F")
    elif(wanted == 2):
        F = float(input("What is the number of degrees fahrenheit to convert to celsius? "))
        print(str(F) + "°F = " + str(F_to_C_converter(F)) + "°C")
    elif(wanted == 3):
        C = float(input("What is the number of degrees kelvin to convert to celsius? "))
        print(str(K) + "°K = " + str(k_to_c_converter(K)) + "°C")
    elif(wanted == 4):
        K = float(input("What is the number of degrees celsius to convert to Kelvin? "))
        print(str(C) + "°C = " + str(c_to_k_converter(CK)) + "°K")

#If file is run as standalone, run main() function
if __name__ == "__main__":
    main()
