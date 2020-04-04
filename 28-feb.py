"""
Program 1: Write a Program that prints whether a number entered by user is
Disarium Number or not.
{Note: A number can be termed as Disarium number if the sum of every digits
raised by their position in that number is equal to that number. E.g. 135, 1 is at
position 1, 3 is at position 2 & 5 is at position 3, then 1^1 + 3^2 + 5^3 = 1 + 9 +
125 = 135, so 135 is a Disarium Number}
Input: 89
Output: 89 is a Disarium Number.

"""
def disarium(num):

    n = str(num)
    temp = 0
    length = len(n)
    for i in range(1,length+1):
        temp +=  pow(int(n[i-1]),i)
    if(temp==num):
        print("{0} is Disarium Number".format(num))
#disarium(89)

"""
Program 2: Write a Program that calculates diameter of a circle if user provides
circumference of the same circle. {Note: π = 3.142}
Input: Circumference of circle = 25.13
Output: Diameter of that circle is 8
"""

def calDia(circum):
    #circumference = pi*dia
    pi = 3.142
    print("Diameter of that circle is {0}".format(round(circum/pi,2)))
#calDia(25.13)

"""
Program 3: Write a Program that accepts a number from user and prints
second minimum digit from that number.
Input: 12357798
Output: The Second minimum Digit from number 112357798 is 2
"""
def secondMin(num):

    num = str(num)
    length = len(num)
    n = [0]*length

    for i in range(length):
        n[i] = int(num[i])
    n.sort()

    min = n[0]

    for i in n:
        if(i>min):
            min = i
            break
    print("The Second minimum Digit from number {0} is {1}".format(num,min))
#secondMin(112357798)

""""
Program 4: Write a Program to Print following Pattern.
0A 1B 2C 3D
1B 2C 3D
2C 3C
3D
"""

def pattern():
    num = 4

    for i in range(num):

        for j in range(num):

            if((i+j)<num):
                print(i+j,end="")
                print(chr(i+j+65),end=" ")
        print()

#pattern()

"""
Program 5: Write a Program calculates Distance between two points of a line,
if user provides Point A & Point B of that line.
{Note: Distance of a line is computed as d(line) =√(x2-x1) 2 + (y2-y1) 2 }
Input:
Point A (x1, y1) = 5 1
Point B (x2, y2) = 8 1
Output: Distance d(AB) = 3
"""

import math
def calDist(x1,y1,x2,y2):
    x = pow((x2-x1),2)
    y = pow((y2-y1),2)

    dist = math.sqrt(x+y)

    print("Distance d(AB) = {0}".format(dist))
calDist(5,1,8,1)