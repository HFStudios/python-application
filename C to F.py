def C_to_F_convertor(C):
    F = (C * 9/5) + 32
    print(F)
#;lsdflksjadf;lskjfl;dkjsa;ldjfm
C = float(input("What is the number of degrees Celcius to conver to Fahrenheit?"))

if (C < -273.15):
    C_to_F_convertor(C)
    print("true")
else:
    print("This is not possible!")
