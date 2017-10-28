import math

#Strings to print out as results
scalene = "Scalene Triangle"
equilateral = "Equilateral Triangle"
right = "Right Triangle"
notTri = "Not a Triangle"
isosceles = "Isosceles Triangle"

#other thing 2
def tri(n):
    x = 1
    if (sideX + sideY > hypotenuse and hypotenuse + sideX > sideY and hypotenuse + sideY > sideX):
        if ((hypotenuse ** 2) == (sideX ** 2) + (sideY ** 2)):
            print(right)
        elif (hypotenuse == sideX == sideY):
            print(equilateral)
        elif (hypotenuse != sideX and hypotenuse != sideY and sideY != sideX):
            print(scalene)
        elif (hypotenuse == sideX or hypotenuse == sideY or sideX == sideY):
            print(isosceles)
        else:
            print(notTri)
    else:
         print(notTri)





#Main part
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
    tri(1)



#Details if wants to use points
else:
    hypotenuse = 0
    x1 = int(input("What is x1? "))
    y1 = int(input("What is y1? "))
    x2 = int(input("What is x2? "))
    y2 = int(input("What is y2? "))
    x3 = int(input("What is x3? "))
    y3 = int(input("What is y3? "))

    dis1 = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    dis2 = math.sqrt(((x3 - x2) ** 2) + ((y3 - y2) ** 2))
    dis3 = math.sqrt(((x3 - x1) ** 2) + ((y3 - y1) ** 2))

    if (dis1 + dis2 > dis3 and dis2 + dis3 > dis1 and dis3 + dis1 > dis2):
        if (dis1 > dis2 and dis1 > dis3):
            hypotenuse = dis1
            if (x1 == x2 == x3 or y1 == y2 == y3):
                print(notTri)
            if ((hypotenuse ** 2) == (dis2 ** 2) + (dis3 ** 2)):
                print(right)
            elif(hypotenuse == dis2 == dis3):
                print(equilateral)
            elif(hypotenuse == dis2 or hypotenuse == dis3 or dis2 == dis3):
                print(isosceles)
            elif(hypotenuse != dis2 and dis2 != dis3 and hypotenuse != dis3):
                print(scalene)
        if (dis2 > dis1 and dis2 > dis3):
            hypotenuse = dis2
            if (x1 == x2 == x3 or y1 == y2 == y3):
                print(notTri)
            if ((hypotenuse ** 2) == (dis1 ** 2) + (dis3 ** 2)):
                print(right)
            elif(hypotenuse == dis1 == dis3):
                print(equilateral)
            elif(hypotenuse == dis1 or hypotenuse == dis3 or dis1 == dis3):
                print(isosceles)
            elif(hypotenuse != dis1 and dis1 != dis3 and hypotenuse != dis3):
                print(scalene)
        if (dis3 > dis1 and dis3 > dis2):
            hypotenuse = dis3
            if (x1 == x2 == x3 or y1 == y2 == y3):
                print(notTri)
            if ((hypotenuse ** 2) == (dis1 ** 2) + (dis2 ** 2)):
                print(right)
            elif(hypotenuse == dis1 == dis2):
                print(equilateral)
            elif(hypotenuse == dis1 or hypotenuse == dis2 or dis1 == dis2):
                print(isosceles)
            elif(hypotenuse != dis1 and dis1 != dis2 and hypotenuse != dis2):
                print(scalene)
    else:
        print(notTri)
