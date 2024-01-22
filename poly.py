# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 02:12:31 2020

@author: abbme
"""

from Coord import *

import time

from time import perf_counter





def isleft(points,L,x):
    l = L[-1]
    v1 = (l[1].x-l[0].x, l[1].y-l[0].y)   # Vector 1
    v2 = (l[1].x-points[x].x, l[1].y-points[x].y)   # Vector 1
    xp = v1[0]*v2[1] - v1[1]*v2[0]  # Cross product
    if xp > 0:
        return False

def convex_poly(points):
    tic = perf_counter()
    q = []
    L = []
    q.append(points[0])
    q.append(points[1])
    y = 0
    t = 1
    x = 2
    while (q[t-1].direction(q[t],points[x]) > 0):
        #print(x)
        x = x + 1
        if x == 2:
            break
    q.append(points[x])
    t = t + 1
    y = x-1
    n = len(points)
    while True:
        x = (x + 1)%n
        if x==2:
            break
        if q[t-1].direction(q[t],points[x]) <= 0:
            if points[y].direction(q[t],points[x]) > 0:
                #print(points[y],q[t],points[x])
                L.append([q[t-1],q[t]])
            else:
                #print('h')
                L.append([q[t],q[0]])
            while isleft(points,L,x):
                x = (x + 1)%n
                if x == 2:
                    break
        if x == 2:
            break
        while q[t-1].direction(q[t],points[x]) > 0:
            q.pop()
            t = t-1
        q.append(points[x])
        t = t+1
        y = (x-1)%n

    toc = perf_counter()
    print("Processing time for Convex hull of a polygon: " + str(toc-tic) + " seconds")
    return q



# points = [] 
# points.append(Point(6, 0)) 
# points.append(Point(2, 0)) 
# points.append(Point(1, 1)) 
# points.append(Point(1, 3)) 
# points.append(Point(2, 4)) 
# points.append(Point(3, 3)) 
# points.append(Point(2, 2))          
# points.append(Point(4, 2)) 
# points.append(Point(4, 4)) 
# points.append(Point(6, 4)) 
# points.append(Point(5, 3)) 


# q = convex_poly(points)

# for each in q:
#     print(each)
    
# # points.append(Point(6, 0)) 
# # points.append(Point(2, 0)) 
# # points.append(Point(1, 1)) 
# # points.append(Point(1, 3)) 
# # points.append(Point(2, 4)) 
# # points.append(Point(4, 4)) 
# # points.append(Point(6, 4)) 
# # points.append(Point(6, 2)) 
