#make a function that does a circle from three points
def circle_from_points(p1, p2, p3):
    #calculate the center of the circle
    #make the average point of the three points
    center = ((p1[0] + p2[0] + p3[0]) / 3, (p1[1] + p2[1] + p3[1]) / 3)
    #calculate the radius of the circle
    radius = math.sqrt((center[0] - p1[0])**2 + (center[1] - p1[1])**2)
    #return the center and radius as a tuple
    return center, radius
    pass   

#call the function
circle_from_points((1, 1), (2, 2), (3, 3))