# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 15:54:24 2020

@author: abbme
"""

from Coord import *
import jarvis as j
import brute as b
import math
from time import perf_counter

# Divide the points by x axis
def divide(points,n,parts):
    points = sort_xy(points,n-1)
    # print("''''''''''''''")
    # for each in points:
    #     print(each)   
    section = n/float(parts)
    if section<3:
        return("Error")
    division = []
    final = 0.0
    while final < n:
        division.append(points[math.floor(final):math.floor(final+section)])
        final = final + section
    return division
# Calculate the convex hulls of each division   
def convex_hull(points,n,parts):
    tic = perf_counter()
    division = divide(points,n,parts)
    if division == "Error":
        return("Error")
    # cn = len(division)
    # for i in division:
    #     print("part")
    #     for each in i:
    #         print(each)

    hulls = []
    for i in division:
        # print(i)
        hullind = j.convex_hull(i, len(i))
        hull = []
        for h in hullind:
            # print(h)
            # print(i)
            hull.append(i[h])
        hulls.append(hull)
    toc = perf_counter()
    return(hulls,toc-tic)

# hulls = convexHull(points,n=len(points),parts=2)

# Get tangent and Merge two hulls together
def mergec(hulls):
    lh = hulls[0]
    rh = hulls[1]
    llen = len(lh)
    rlen = len(rh)
    righthull = leftmost(rh,len(rh))
    lefthull = rightmost(lh,len(lh))
    ri = righthull
    li = lefthull
    # print(li)
    # print(ri) 
    # Upper tangent
    # http://www.cs.tulane.edu/~carola/teaching/cmps6610/fall16/slides/Lecture-divideAndConquer.pdf
    while lh[li].direction(rh[ri],rh[(ri+1)%rlen]) > 0 or lh[(li-1)%llen].direction(lh[li],rh[ri]) > 0:
        while lh[li].direction(rh[ri],rh[(ri+1)%rlen]) > 0:
            ri = (ri+1)%rlen
        while lh[(li-1)%llen].direction(lh[li],rh[ri]) > 0:
            li = (li-1)%llen
    ul = li
    ur = ri
    ri = righthull
    li = lefthull
    # Lower tangent
    while lh[li].direction(rh[ri],rh[(ri-1)%rlen]) < 0 or lh[(li+1)%llen].direction(lh[li],rh[ri]) < 0:
        while lh[li].direction(rh[ri],rh[(ri-1)%rlen]) < 0:
            ri = (ri-1)%rlen
        while lh[(li+1)%llen].direction(lh[li],rh[ri]) < 0:
            li = (li+1)%llen 
    ll = li
    lr = ri
    # print(lh[ul])
    # print(rh[ur])
    # print(lh[ll])
    # print(rh[lr])
    newhull = []
    # Merge the hulls
    newhull.append(lh[ul])
    newhull.append(rh[ur])
    ind = ur
    while ind!=lr:
        ind = (ind+1)%rlen
        newhull.append(rh[ind])
    # for each in newhull:
    #     print(each)
    # print()
    ind = ll
    while ind!=ul:
        newhull.append(lh[ind])
        ind = (ind+1)%len(lh)
    # for each in newhull:
    #     print(each)
    return newhull

# Feed the hulls into the merge function and combine them.
def conquer(hulls):
    tic2 = perf_counter()
    # for each in hulls:
    #         print(each)
    #         print()
    n = len(hulls)
    for i in range(n-1):
        # print("lenhull"+str(len(hulls)))
        # print(hulls[-2:])      
        conquered = mergec(hulls[-2:])
        hulls = hulls[0:-2]
        hulls.append(conquered)
        # print(i)
        # print(hulls)
    toc2 = perf_counter()
    return hulls,(toc2-tic2)


    


    

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


# hulls,time = convex_hull(points, len(points), 3)

# newhulls,time2 = conquer(hulls)
# # # # print(hulls)
# # # # len(hulls)
# # # # hulls[-2:]
# for i in newhulls:
#     for j in i:
#         print(j)



# # # a = [0,1,2,3,4,5]
# # # del a[4:-1]

# # # a