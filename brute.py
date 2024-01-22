# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 14:25:53 2020

@author: abbme
"""

# Outputs two index lists of convex hull point pairs.
# Coded directly from the pseudocode
# class Point: 
#     def __init__(self, x, y): 
#         self.x = x 
#         self.y = y 

import time
# Returns 1 if a pair of points are a part of convex hull       
def inhull(points,i,j,n):
    p_above = 0
    p_below = 0
    x1, x2, y1, y2 = points[i].x, points[j].x, points[i].y, points[j].y
    a = y2-y1
    b = x1-x2
    c = (x1*y2-x2*y1)/1.0
    for p in range(n):
        # Check if all points lie below or above the pair
        if(i!=p and j!=p):
            if(a*points[p].x + b*points[p].y - c < 0):
                # print(a*points[p].x + b*points[p].y - c) 
                p_below += 1
            if(a*points[p].x + b*points[p].y - c > 0):  
                p_above += 1    
    if(p_above == (n-2) or p_below ==(n-2)):
        return 1
    else:
        return 0

def convex_hull(points,n):
    h1 = []
    h2 = []
    if n < 3: 
        return
    tic = time.perf_counter()
    for i in range(n):
        for j in range(i,n):
            # print(i,j)
            c = inhull(points,i,j,n)
            if c == 1:
                # print(c)
                h1.append(i)
                h2.append(j)
    toc = time.perf_counter()
    print("Processing time for Brute Force convex hull: " + str(toc-tic) + " seconds")
    return h1,h2


      
# points = [] 
# points.append(Point(0, 3)) 
# points.append(Point(2, 2)) 
# points.append(Point(1, 1)) 
# points.append(Point(2, 1)) 
# points.append(Point(3, 0)) 
# points.append(Point(0, 0)) 
# points.append(Point(3, 3))             

# hx,hy = convexHull(points,len(points))
# print(hx,hy)

# 0,3 - 0,0
# 0,3 - 3,3
# 3,0 - 0,0
# 3,0 - 3,3