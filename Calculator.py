opp = input(print("what opporation?"))
if opp == "+":
    num1 = int(input(print("what is your first number?")))
    num2 = int(input(print("what is your second number?")))
    print(num1 + num2)
elif opp == "-":
    num1 = int(input(print("what is your first number?")))
    num2 = int(input(print("what is your second number?")))
    print(num1 - num2)
elif opp == "*":
    num1 = int(input(print("what is your first number?")))
    num2 = int(input(print("what is your second number?")))
    print(num1*num2)
elif opp == "/":
    num1 = int(input(print("what is your first number?")))
    num2 = int(input(print("what is your second number?")))
    if num2 == 0:
        print("can't divid by zero!!")
        while num2 == 0:
            num2 = int(input(print("what is your second number?")))
    print(num1 / num2)
elif opp == "^" or "**":
    num1 = int(input(print("what is the base number?")))
    num2 = int(input(print("what is the power?")))
    print(num1 ** num2)
#i will add trig functions later!!
