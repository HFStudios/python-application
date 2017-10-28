import math

#Strings to print out as results
scalene = "Scalene Triangle"
equilateral = "Equilateral Triangle"
right = "Right Triangle"
notTri = "Not a Triangle"
isosceles = "Isosceles Triangle"

#Runs if user gives side lengths instead of points
def givenLengths(side1, side2, side3):
    #Makes it so that the lengths can be put in any order and still get the right results
    l1 = max(side1, side2, side3)
    l3 = min(side1, side2, side3)
    l2 = (side1 + side2 + side3) - l1 - l3

    #Finds out what type of triangle it is
    if (((l2 + l3) > l1) and ((l1 + l2) > l3) and ((l1 + l3) > l2)):
        if ((l1 ** 2) == (l2 ** 2) + (l3 ** 2)):
            return right
        elif (l1 == l2 == l3):
            return equilateral
        elif ((l1 != l2) and (l1 != l3) and (l3 != l2)):
            return scalene
        elif ((l1 == l2) or (l1 == l3) or (l2 == l3)):
            return isosceles
        else:
            return notTri
    else:
         return notTri

#Runs if user gives points instead of side lengths
def givenPoints(x1, y1, x2, y2, x3, y3):
    #Gets length of sides, plugs into givenLengths() to get triangle type
    dist1 = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    dist2 = math.sqrt(((x3 - x2) ** 2) + ((y3 - y2) ** 2))
    dist3 = math.sqrt(((x3 - x1) ** 2) + ((y3 - y1) ** 2))

    triType = givenLengths(dist1, dist2, dist3)
    return(dist1, dist2, dist3, triType)


#Runs terminal version of program
def main():
    #Find out if user wants to use points or lengths of sides
    while True:
        getInput = input("Find the triangle with lengths (1) or points (2)? ")
        if(getInput == "lengths" or getInput == "1"):
            wanted = 1
            break
        elif(getInput == "points" or getInput == "2"):
            wanted = 2
            break
        else:
            print("Choose a real selection: ")

    #Ask details about side lenths
    if (wanted == 1):
        side1 = float(input("What is side 1? "))
        side2 = float(input("What is side 2? "))
        side3 = float(input("What is side 3? "))
        print(givenLengths(side1, side2, side3))

    #Details if wants to use points
    else:
        x1 = float(input("What is x1? "))
        y1 = float(input("What is y1? "))
        x2 = float(input("What is x2? "))
        y2 = float(input("What is y2? "))
        x3 = float(input("What is x3? "))
        y3 = float(input("What is y3? "))
        print(givenPoints(x1, y1, x2, y2, x3, y3))


#If file is run as standalone, run main() function
if __name__ == "__main__":
    main()
