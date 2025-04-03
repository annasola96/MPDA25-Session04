from typing import cast, Any

import Rhino.Geometry as rg #type:ignore
import ghpythonlib.treehelpers as th #this library is needed to import nested lists to grasshopper trees
import math #this library is needed to create sine and cosine waves
import System

# DECLARE INPUT VARIABLES OF PYTHON COMPONENT
x_points = cast(int, x_points)  # type: ignore
y_points = cast(int, y_points)  # type: ignore

#START CONDING HERE 

#1.- create first series of points -
#start by initializing an empty list and fill it with points 
#by creating points with a for loop. The number of points should come 
#from a grasshopper slider called x_points (remember to set the type)
#Increment the X coordinate of the point at each iteration so to create
#a series of points along the X axis line
#store that point to the list
#output this list to grasshopper to verify the result should look like gh component (1.)

pointList1 = []
for i in range(x_points):
    pointList1.append(rg.Point3d(i, 0, 0)) 

a = pointList1

#2. - create second series of points -
#create a second list of points  by copying the code above, but this time
#assign the Y coordinate of each point to a value that comes from an 
#external input which can be a slider in grasshopper called y_points
#output that list as well, the result should look like component (2.) 

pointList2 = []
for i in range(x_points):
    pointList2.append(rg.Point3d(i, y_points, 0))

b = pointList2

#3. - create lines from two serie of points - 
#initialize another empty list to store some lines
#make another for loop that iterates through each point in any of the list BY INDEX
#within this loop, make a line that draws from points in both lists with the same index
#and append that line to the line list. output the result
#hint: you only need one for loop for this

lineList = []
for i in range(x_points):
    lineList.append(rg.LineCurve(a[i], b[i]))

c = lineList

#4.- divide curve -
#initialize another empty list to store some curves
#interate through every line in the line list with a for loop 
#inside the scope of this for loop, create an empty list to store the division points
#inside the for loop, convert each line to a nurbs curve, like shown in class
#divide the new curve into 10 points by applying DivideByCount() method (see rhinocommo) and store the result
#this returns a list of parameters in the line which correspond to each parameter
#you need to iterate through the list of params with another for loop and get the point per each param 
#using Line.PointAt(), and there the points in the list of divison points

allDivPts = [] #this will be a list of lists
for line in lineList:
    linePts =[] #create an empty list to fill each iteration

    params = line.DivideByCount(10, True) #divide the line into 10 points    
    for p in params:
        divPt = line.PointAt(p) #get the point per each param        
        linePts.append(divPt)

    #here you return to the scope of the first for loop
    allDivPts.append(linePts) #append the list of points PER LINE to another list

d = th.list_to_tree(allDivPts) #this is how you output nested lists to gh trees