"""
Program 1: Write a Program that prints the Series of palindrome ranging in 300
to 600
Output: 313, 323, 333, 343 . . .
"""

def pallindrome():

    for i in range(300,600):
            i = str(i)
            flag = 0
            length = len(i)
            for j in range(int(length/2)):
                if(i[j]!=i[length-j-1]):
                    flag=1
                    break
            if(flag==0):
                print(i)
#pallindrome()

"""
Program 2: Write a Program that calculates Square Root of a number ranging
in 200 to 600
"""
import math
def squareRoot():
    for i in range(200,600):
        print("Square Root of {0} is {1}".format(i,math.sqrt(i)))
#squareRoot()

"""
Program 3: Write a Program that accepts a number from user and prints
minimum digit from that number.
Input: 12357798
Output: The Min Digit from number 12357798 is 1
"""
def minDigit():
    n = input()
    min = int(n[0])

    for i in n:
        if(min>int(i)):
            min = int(i)
    print(min)
#minDigit()

"""
Program 4: Write a Program to Print following Pattern.
* * * *
* * *
* *
*
"""

def pattern():
    num = 4

    for i in range(num):
        for j in range(num):

            if((i+j)<num):
                print("*",end=" ")
        print("")
#pattern()

"""
Program 5: Write a Program calculates mid-point of a line made up of two
points where user provides the two points.
Input:
Enter Point A (x1, y1) = 4 5
Enter Point B (x2, y2) = 2 4
Output: Mid-Point of Line AB = (3, 4.5)
"""

def midpoint(x1,y1,x2,y2):

    x = (x1+x2)/2
    y = (y1+y2)/2

    x = "%.1f"%x
    y = "%.1f"%y

    print("Mid-Point of Line AB = ({0}, {1})".format(x,y))
midpoint(4,5,2,4)