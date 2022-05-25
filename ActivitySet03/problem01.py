# Problem 1: Rectangle Area
# Develop a program that, given as input the cartesian coordinates of three vertices of a Rectangle,
# reports the area of that Rectangle. You will recall that the area of a Rectangle is the product of
# the lengths of any two adjacent sides.
# Input: The first line contains a positive integer n indicating how many Rectangles are to be
# analyzed. Each Rectangle is described on a single line via six real numbers, x1, y1, x2, y2, x3,
# and y3, separated by spaces. These provide the coordinates of three of the Rectangle’s vertices,
# namely P1(x1, y1), P2(x2, y2), and P3(x3, y3).
# Output: For each Rectangle provided as input, report its area.
# Sample input
# ------------
# 3
# 0.0 0.0 0.0 1.0 1.0 0.0
# -1.0 2.0 3.0 5.0 1.0 1.0
# 5.0 9.0 -0.5 0.0 7.5 5.0
# Resultant output
# ----------------
# Area of Rectangle with vertices (0.0,0.0),(0.0,1.0),(1.0,0.0) is 1.0
# Area of Rectangle with vertices (-1.0,2.0),(3.0,5.0),(1.0,1.0) is 10.0
# Area of Rectangle with vertices (5.0,9.0),(-0.5,0.0),(7.5,5.0) is 44.5
from math import *
n=int(input("Enter limit:"))
for i in range(0,n):
    
    x1,y1,x2,y2,x3,y3=input().split()
    (X1,Y1,X2,Y2,X3,Y3)=(float(x1),float(y1),float(x2),float(y2),float(x3),float(y3))
    area_Rectangle=2*(0.5*fabs((((X1*(Y2-Y3))+(X2*(Y3-Y1))+(X3*(Y1-Y2))))))
    print("Area of Rectangle with vertices (%0.1f,%0.1f),(%0.1f,%0.1f),(%0.1f,%0.1f) is %0.1f\n"%(X1,Y1,X2,Y2,X3,Y3,area_Rectangle))
    

    


