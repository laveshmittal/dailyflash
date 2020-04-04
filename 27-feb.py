"""
Program 1: Write a Program that prints the Series of palindrome bounding
between limits entered by user.
Input:
Lower Bound: 300
Upper Bound: 350
Output: 303, 313, 323, 333, 343
"""
def pallindrome(lower,upper):

    for i in range(lower,upper):

        i = str(i)
        flag = 0
        length = len(i)
        for j in range(int(length/2)):
            if(i[j]!=i[length-j-1]):
                flag=1

        if(flag==0):
            print(i)

#lower = int(input("Lower Bound:"))
#upper = int(input("Upper Bound:"))
#pallindrome(lower,upper)

"""
Program 2: Write a Program that calculates radius of a circle if user provides
the area covered by that circle.
Input: Area of Circle 50.27
Output: Radius of circle is 4
"""
import math
def calRadius(area):
    pi = math.pi
    print("Radius of circle is {0}".format(round(math.sqrt(area/pi),2)))
#calRadius(50.27)

"""
Program 3: Write a Program that accepts a number from user and prints
second Maximum digit from that number.
Input: 12357798
Output: The Second Maximum Digit from number 12357798 is 8
"""
def secondMax(num):
    num = str(num)
    n = [0]*len(num)
    for i in range(len(num)):
        n[i] = int(num[i])
    n.sort(reverse=True)

    print("The Second Maximum Digit from number {0} is {1}".format(num,n[1]))
#secondMax(12357798)

"""
Program 4: Write a Program to Print following Pattern.
A B D G
G J K
J K
K
"""

def pattern():
    """
    To get the ASCII code of a character, use the ord() function. To get the character encoded by an ASCII code number, use the chr() function.

    """
    num = 4
    ascii_start =temp = 65
    for i in range(num):
        for j in range(num-i):
            temp = temp + j
            print(chr(temp),end=" ")
        print()
#pattern()

"""
Program 5: Write a Program calculates slope of a line if user provides the Two
Points A & B of that line.
{Note: Slope of a line is computed as m = ((y2-y1)/(x2-x1)) }
Input:
Point A (x1, y1) = 5 2
Point B (x2, y2) = 8 1
Output: Slope of line AB is 3
"""

def calSlope(x1,y1,x2,y2):

    x = x2-x1
    y = y2-y1

    slope = y/x

    print("Slope of line AB is {0}".format(round(slope,2)))
#calSlope(5,2,8,1)