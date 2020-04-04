"""
Program 1: Write a Program that prints the Disarium Number limiting between
bounds provided by user.
Input:
Lower Bound: 1
Upper Bound: 100
Output: Series of Disarium Number ranging in 1 to 100 is = 1 2 3 4 5 6 7 8 9 89
"""

def disariumSeries(lower,upper):
    s = []
    for i in range(lower,upper):
        temp = 0
        i = str(i)
        for j in range(1,len(i)+1):
            temp += pow(int(i[j-1]),j)

        if(temp==int(i)):
          s.append(temp)

    print("Series of Disarium Number ranging in {0} to {1} is = ".format(lower,upper),end=" ")
    for i in s:
        print(i , end=" ")

#disariumSeries(1,100)

"""
Program 2: Write a Program that accepts a number from user and prints the
values at following places from that number. {Value at one’s place, ten’s place,
hundreds’ place & thousand’s place if the values exists}
Input: 123
Output:
Value at ones place: 3
Value at ten’s place: 2
Value at hundreds’’ place: 1
"""
def printValue(num):

    num = str(num)
    length = len(num)

    if(length>=1):
        print("Value at ones place:",num[-1])
    if(length>=2):
        print("Value at ten's place:",num[-2])
    if (length >= 3):
        print("Value at hundered's place:", num[-3])
    if (length >= 4):
        print("Value at thousand's place:", num[-4])
#printValue(1234)

"""
Program 3: Write a Program that accepts a number from user and prints
minimum & maximum digit from that number.
Input: 12357798
Output: Minimum Digit is 1 & Maximum Digit is 9
"""

def minMax(num):

    num = str(num)
    s = []
    for i in range(len(num)):
        s.append(int(num[i]))

    s.sort()

    print("Minimum Digit is {0} & Maximum Digit is {1}".format(s[0],s[-1]))

#minMax(12357798)


"""
Program 4: Write a Program to Print following Pattern.
0 1 0 1
0 1 0
0 1 
0
"""

def pattern():
    num = 4

    for i in range(num):
        for j in range(num):

            if((i+j)<num):

                if(j==0 or j%2==0):
                    print(0,end=" ")
                else:
                    print(1,end=" ")
        print()
#pattern()

"""
Program 5: Write a Program calculates length of all three sides of a triangle if
user provides the three points that triangle bound in.
{Note: Use Distance formula for computing the distances.}
Input:
A (x1, y1) = 5 2
B (x2, y2) = 6 3
C (x3, y3) = 3 1
Output:
Length AB = 1.41
Length BC = 3.61
Length AC = 2.24
"""
import math
def dist(x1,y1,x2,y2):
    x = x2-x1
    y = y2-y1

    dist = math.sqrt(pow(x,2)+pow(y,2))
    dist = abs(dist)
    return dist



def calSides(x1,y1,x2,y2,x3,y3):

    s1 = dist(x1,y1,x2,y2)
    s2 = dist(x2,y2,x3,y3)
    s3 = dist(x1,y1,x3,y3)
    s1 = "%.2f"%s1
    s2 = "%.2f" % s2
    s3 = "%.2f" % s3
    print("Length AB = {0}",format(s1))
    print("Length BC = {0}",format(s2))
    print("Length AC = {0}",format(s3))
calSides(5,2,6,3,3,1)