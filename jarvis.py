# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 15:44:01 2020

@author: abbme
"""

# Input x and y is attribute of Point object
# Returns two lists containing both the x and y coordinates of the hull
import time
from Coord import Point,leftmost 

# https://en.wikipedia.org/wiki/Gift_wrapping_algorithm

    
def convex_hull(points,n):
    # Generate convex hull using jarvis algorithm
    tic = time.perf_counter()
    hull = []
    l = leftmost(points, n)
    first = l
    while(True):
        hull.append(l)
        # Select the point after l in the list until we reach the first point
        r = (l + 1)%n
        for i in range(n):
            # Check if points l->i->r turn right and if they do
            # make i the new leftmost point
            if r == l or points[l].direction(points[i],points[r]) < 0:
                r = i
        # The new leftmost point is added to the hull
        l = r
        # if the leftmost point is same as the first point in hull, break from loop
        if l == first:
            break
    toc = time.perf_counter()
    print("Processing time for Jarvis convex hull: " + str(toc-tic) + " seconds")
    return hull
        
    
# points = [] 





# for i in h:
#     print(points[i].x,points[i].y)


# points = [] 
# points.append(Point(0, 3)) 
# points.append(Point(2, 2)) 
# points.append(Point(1, 1)) 
# points.append(Point(2, 1)) 
# points.append(Point(3, 3)) 
# points.append(Point(0, 0)) 
# points.append(Point(3, 0))          
# points.append(Point(5, 1)) 
# points.append(Point(7, 4)) 
# points.append(Point(2, 9)) 

# h = convex_hull(points, len(points))
# for i in h:
#     print(points[i])