#-*- coding: utf-8 -*-
"""
Created on Sun Nov 8 2020
@author: zyadb
"""

"""
pseudocode : Graham scan (wikipedia)
•	Select the point with minimum 𝑦
•	Sort all points in CCW order {𝑝0, 𝑝1, … , 𝑝𝑛}
•	𝑆 = {𝑝0, 𝑝1}
•	For 𝑖 = 2 to 𝑛
o	    While |𝑆| > 2 && 𝑝𝑖 is to the right of 𝑆−2, 𝑆−1
	        𝑆.pop
o	    𝑆.push(𝑝𝑖)

"""
import time
import math
from math import atan2 # for computing polar angle
from Coord import Point 

"""
# Select the point with minimum 𝑦
"""
def lowest_y(points):
    miny = points[0].y
    minind = 0
    for i, point in enumerate(points):
        if point.y < miny:
            miny = point.y
            minind = i
        if point.y == miny:
            if point.x < points[minind].x:
                minind = i

    return points[minind], minind

def euc_dist(p0,p1,p2):
    d1=math.sqrt((p1.x-p0.x)**2 + (p1.y-p0.y)**2)
    d2=math.sqrt((p2.x-p0.x)**2 + (p2.y-p0.y)**2)
    return d1, d2

"""
# 2. Sort all points in CCW order {𝑝0, 𝑝1, … , 𝑝𝑛}
"""
def polar_angle_sort(points,p0):
    sorted_angle = {}
    sorted_index = []
    sorted_points = []
    #calculate the polar angle with p0 for all points
    for i,point in enumerate(points):
        if point == p0:
            pass
        else:
            vec_x=point.x-p0.x
            vec_y=point.y-p0.y
            #keeping index to find initial points
            sorted_angle[i] = math.atan2(vec_y, vec_x) 


    #sort angles (gives a list)
    sorted_angle=sorted(sorted_angle.items(), key=lambda x: x[1], reverse=False)
    #transform sorted list to dict
    sorted_angle={sorted_angle[i][0]: sorted_angle[i][1] for i in range(0, len(sorted_angle))}
    #get sorted index of points from sorted angle dict
    sorted_index=sorted_angle.keys()
    
    #sort points with sorted index
    for i,index in enumerate(sorted_index):
        sorted_points.append(points[index])

    # We remove collinear points with p0 and keep only furthest
    coll_points = []
    for i in range(len(sorted_points) - 1):
        d = p0.direction(sorted_points[i],sorted_points[i+1])
        if d == 0:
            coll_points.append(i)
    sorted_points = [i for j, i in enumerate(sorted_points) if j not in coll_points]

    return sorted_points

"""
For 𝑖 = 2 to 𝑛
o	    While |𝑆| > 2 && 𝑝𝑖 is to the right of 𝑆−2, 𝑆−1
	        𝑆.pop
o	    𝑆.push(𝑝𝑖)
end
"""
def convex_hull(points):
    tic = time.perf_counter()
    p0, minind = lowest_y(points)
    points = polar_angle_sort(points,p0)
    convex_hull = []
    convex_ind = []
    
    #P0 and the first point in the sorted list are automatically in the convex hull
    convex_hull.append(p0)
    convex_hull.append(points[0])
    convex_hull.append(points[1])
    convex_ind.append(minind)
    
    m = 3
    for i in range(2,len(points)):
        while True:
            direction = convex_hull[m-2].direction(convex_hull[m-1],points[i])
            if direction > 0:
                break            
            else:
                convex_hull.pop()
                m -= 1
        convex_hull.append(points[i])
        m += 1
    '''
    for i,p in enumerate(convex_hull):
        print(p)
    '''
    toc = time.perf_counter()
    print("Processing time for Graham scan convex hull: " + str(toc-tic) + " seconds")
    return convex_hull  # This needs to be an index of points


# points = [] 
# points.append(Point(0, 3)) 
# points.append(Point(2, 2)) 
# points.append(Point(1, 1)) 
# points.append(Point(2, 1)) 
# points.append(Point(3, 3)) 
# points.append(Point(0, 0)) 
# points.append(Point(3, 0))     




# print(convex_hull(points))