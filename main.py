import math

#Strings to print out as results
scalene = "Scalene Triangle"
equilateral = "Equilateral Triangle"
right = "Right Triangle"
notTri = "Not a Triangle"
isosceles = "Isosceles Triangle"

#Runs if user gives side lengths instead of points
def givenLengths(hypotenuse, sideX, sideY):

    x = 1

    if (((sideX + sideY) > hypotenuse) and ((hypotenuse + sideX) > sideY) and ((hypotenuse + sideY) > sideX)):
        if ((hypotenuse ** 2) == (sideX ** 2) + (sideY ** 2)):
            return right
        elif (hypotenuse == sideX == sideY):
            return equilateral
        elif ((hypotenuse != sideX) and (hypotenuse != sideY) and (sideY != sideX)):
            return scalene
        elif ((hypotenuse == sideX) or (hypotenuse == sideY) or (sideX == sideY)):
            return isosceles
        else:
            return notTri
    else:
         return notTri

#Runs if user gives points instead of side lengths
def givenPoints(x1, y1, x2, y2, x3, y3):

    hypotenuse = 0

    dis1 = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    dis2 = math.sqrt(((x3 - x2) ** 2) + ((y3 - y2) ** 2))
    dis3 = math.sqrt(((x3 - x1) ** 2) + ((y3 - y1) ** 2))

    if (dis1 + dis2 > dis3 and dis2 + dis3 > dis1 and dis3 + dis1 > dis2):
        if (dis1 > dis2 and dis1 > dis3):
            hypotenuse = dis1
            if (x1 == x2 == x3 or y1 == y2 == y3):
                return notTri
            if ((hypotenuse ** 2) == (dis2 ** 2) + (dis3 ** 2)):
                return right
            elif(hypotenuse == dis2 == dis3):
                return equilateral
            elif(hypotenuse == dis2 or hypotenuse == dis3 or dis2 == dis3):
                return isosceles
            elif(hypotenuse != dis2 and dis2 != dis3 and hypotenuse != dis3):
                return scalene

        if (dis2 > dis1 and dis2 > dis3):
            hypotenuse = dis2
            if (x1 == x2 == x3 or y1 == y2 == y3):
                return notTri
            if ((hypotenuse ** 2) == (dis1 ** 2) + (dis3 ** 2)):
                return right
            elif(hypotenuse == dis1 == dis3):
                return equilateral
            elif(hypotenuse == dis1 or hypotenuse == dis3 or dis1 == dis3):
                return isosceles
            elif(hypotenuse != dis1 and dis1 != dis3 and hypotenuse != dis3):
                return scalene

        if (dis3 > dis1 and dis3 > dis2):
            hypotenuse = dis3
            if (x1 == x2 == x3 or y1 == y2 == y3):
                return notTri
            if ((hypotenuse ** 2) == (dis1 ** 2) + (dis2 ** 2)):
                return right
            elif(hypotenuse == dis1 == dis2):
                return equilateral
            elif(hypotenuse == dis1 or hypotenuse == dis2 or dis1 == dis2):
                return isosceles
            elif(hypotenuse != dis1 and dis1 != dis2 and hypotenuse != dis2):
                return scalene
    else:
        return notTri

#Runs terminal version of program
def main():
    wanted = 0

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
        hypotenuse = int(input("What is the hypotenuse? "))
        sideX = int(input("What is side X? "))
        sideY = int(input("What is side Y? "))
        print(givenLengths(hypotenuse, sideX, sideY))

    #Details if wants to use points
    else:
        x1 = int(input("What is x1? "))
        y1 = int(input("What is y1? "))
        x2 = int(input("What is x2? "))
        y2 = int(input("What is y2? "))
        x3 = int(input("What is x3? "))
        y3 = int(input("What is y3? "))
        print(givenPoints(x1, y1, x2, y2, x3, y3))


#If file is run as standalone, run main() function
if __name__ == "__main__":
    main()
