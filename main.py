import math


def tri(n):
    x = 1
    if (length2 + length3 > hy and hy + length2 > length3 and hy + length3 > length2):
        if ((hy ** 2) == (length2 ** 2) + (length3 ** 2)):
            print("Right Triangle")
        elif (hy == length2 == length3):
            print("Equalatoral Trangle")
        elif (hy != length2 and hy != length3 and length3 != length2):
            print("Scalene Triangle")
        elif (hy == length2 or hy == length3 or length2 == length3):
            print("Isosceles Trangle")
        else:
            print("Not a Triangle")
    else:
         print("Not a Triangle")




wanted = 0

while True:
    getInput = input("Find the triangle with length or points? ")
    if(getInput == "length" or getInput == "1"):
        wanted = 1
        break
    elif(getInput == "points" or getInput == "2"):
        wanted = 2
        break
if (wanted == 1):
    hy = int(input("what is hypotenuse? "))
    length2 = int(input("what is length2? "))
    length3 = int(input("what is length3? "))
    tri(1)

else:
    hy = 0
    x1 = int(input("what is x1? "))
    y1 = int(input("what is y1? "))
    x2 = int(input("what is x2? "))
    y2 = int(input("what is y2? "))
    x3 = int(input("what is x3? "))
    y3 = int(input("what is y3? "))

    dis1 = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    dis2 = math.sqrt(((x3 - x2) ** 2) + ((y3 - y2) ** 2))
    dis3 = math.sqrt(((x3 - x1) ** 2) + ((y3 - y1) ** 2))

    if (dis1 + dis2 > dis3 and dis2 + dis3 > dis1 and dis3 + dis1 > dis2):
        if (dis1 > dis2 and dis1 > dis3):
            hy = dis1
            if (x1 == x2 == x3 or y1 == y2 == y3):
                print("Not a Triangle")
            if ((hy ** 2) == (dis2 ** 2) + (dis3 ** 2)):
                print("Right Triangle")
            elif(hy == dis2 == dis3):
                print("Equilateral Triangle")
            elif(hy == dis2 or hy == dis3 or dis2 == dis3):
                print("Isosceles Triangle")
            elif(hy != dis2 and dis2 != dis3 and hy != dis3):
                print("Scalene Triangle")
        if (dis2 > dis1 and dis2 > dis3):
            hy = dis2
            if (x1 == x2 == x3 or y1 == y2 == y3):
                print("Not a Triangle")
            if ((hy ** 2) == (dis1 ** 2) + (dis3 ** 2)):
                print("Right Triangle")
            elif(hy == dis1 == dis3):
                print("Equilateral Triangle")
            elif(hy == dis1 or hy == dis3 or dis1 == dis3):
                print("Isosceles Triangle")
            elif(hy != dis1 and dis1 != dis3 and hy != dis3):
                print("Scalene Triangle")
        if (dis3 > dis1 and dis3 > dis2):
            hy = dis3
            if (x1 == x2 == x3 or y1 == y2 == y3):
                print("Not a Triangle")
            if ((hy ** 2) == (dis1 ** 2) + (dis2 ** 2)):
                print("Right Triangle")
            elif(hy == dis1 == dis2):
                print("Equalatoral Triangle")
            elif(hy == dis1 or hy == dis2 or dis1 == dis2):
                print("Isosceles Triangle")
            elif(hy != dis1 and dis1 != dis2 and hy != dis2):
                print("Scalene Triangle")
    else:
        print("Not a Triangle")
