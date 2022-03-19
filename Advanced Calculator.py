#Coding Advanced Calculator with math and time moduls
import math
import time

print("""
***CALCULATOR***\n
1-Addition
2-Subtraction
3-Multiplication
4-Division
5-Exponential Function
6-Square Root
7-Convert from Degrees to Radians
8-Convert from Radians to Degrees
9-Find to Sine
10-Find to Cosine
11-Find to Tangent
12-Find to Cotangent
13-Logarithm
Tap q for exit from program...\n
""")


while True:
    act = input("Select an action:")
    if(act == 'q'):
        print("Exiting..")
        time.sleep(1)
        print("We are waiting for you again..")
        break
    elif(act == "1"):
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
        print("Calculating..")
        time.sleep((1))
        print("Result: {}".format(number1 + number2))
    elif(act == "2"):
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
        print("Calculating..")
        time.sleep((1))
        print("Result: {}".format(number1 - number2))
    elif(act == "3"):
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
        print("Calculating..")
        time.sleep(1)
        print("Result: {}".format(number1 * number2))
    elif(act == "4"):
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
        print("Calculating..")
        time.sleep(1)
        print("Result: {}".format(number1 / number2))
    elif(act == "5"):
        base = int(input("Enter base: "))
        exponent = int(input("Enter exponent: "))
        print("Calculating..")
        time.sleep(1)
        print("Result: {}".format(pow(base,exponent)))
    elif(act == "6"):
        squareroot = int(input("Enter a number to get the square root: "))
        print("Calculating..")
        time.sleep(1)
        print("Result: {}".format(math.sqrt((squareroot))))
    elif(act == "7"):
        degree = int(input("Enter degree: "))
        print("Calculating..")
        time.sleep(1)
        print("Radian: {}".format(math.degrees(degree)))
    elif(act == "8"):
        radian = int(input("Enter radian: "))
        print("Calculating..")
        time.sleep(1)
        print("Degree: {}".format(math.radians(radian)))
    elif(act == "9"):
        a = input("for radians enter r or R\nfor degrees enter d or D ")
        if(a == "r" or "R"):
            sine = int(input("Enter a degree for find to sine:"))
            print("Calculating..")
            time.sleep(1)
            print("sine({}): {}".format(sine,math.sin(sine)))
        elif(a == "d" or "D"):
            sine = int(input("Enter a radian for find to sine:"))
            print("Calculating..")
            time.sleep(1)
            print("sine({}): {}".format(sine,math.sin((math.radians((sine))))))
        else:
            print("We are not found this process")
            break
    elif(act == "10"):
        a = input("for radians enter r or R\nfor degrees enter d or D ")
        if (a == "r" or "R"):
            cosine = int(input("Enter a degree for find to cosine:"))
            print("Calculating..")
            time.sleep(1)
            print("cosine({}): {}".format(cosine, math.cos(cosine)))
        elif (a == "d" or "D"):
            cosine = int(input("Enter a radian for find to cosine:"))
            print("Calculating..")
            time.sleep(1)
            print("cosine({}): {}".format(cosine, math.cos((math.radians((cosine))))))
        else:
            print("We are not found this process")
            break
    elif(act == "11"):
        tan = int(input("Enter a degree for find to tangent: "))
        print("Calculating..")
        time.sleep(1)
        print("Tangent({}): {}".format(tan,math.tan((tan))))
    elif(act == "12"):
        cot = int(input("Enter a degree for find to cotangent: "))
        print("Calculating..")
        time.sleep(1)
        print("Cotangent({}): {}".format(cot,math.cos(cot) / math.sin(cot)))
    elif(act == "13"):
        base = int(input("Enter a log's base: "))
        exponent = int(input("Enter a log's exponent: "))
        print("Calculating..")
        time.sleep(1)
        print("Result: {}".format(math.log(exponent,base)))
    else:
        print("We are not found this process")
        break






