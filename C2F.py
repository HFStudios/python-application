def C_to_F_converter(C):
    F = (C * (9 / 5)) + 32
    return F

def main():
    C = float(input("What is the number of degrees Celcius to conver to Fahrenheit?"))

    if (C < -273.15):
        print(C_to_F_converter(C))
    else:
        print("This is not possible!")


#If file is run as standalone, run main() function
if __name__ == "__main__":
    main()
