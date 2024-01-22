# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 14:53:30 2020

@author: abbme
"""


class Point: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
     
    def direction(self, pj, pk):
        # Returns direction of three points        
        # Get cross product of vectors to get direction
        x0,x1,x2 = self.x,pj.x,pk.x
        y0,y1,y2 = self.y,pj.y,pk.y
        d = (x1-x0)*(y2-y0)-(x2-x0)*(y1-y0)
        return d
        # d < 0 : points turn left, d > 0 : points turn right, d = 0 points collinear
        # if d < 0:
        #     return -1
        # if d > 0:
        #     return 1
        # if d == 0:
        #     return -1
        # else:
        #     return 1
        
    
    def __str__(self):
        return "x: " + str(self.x) + " y: " + str(self.y) + "\n"
    
def leftmost(points,n): 
    # Returns index of the first leftmost and lowest point in points list
    minx = points[0]
    minind = 0
    for i in range(n):
        if minx.x > points[i].x:
            minx = points[i]
            minind = i
        elif minx.x == points[i].x:
            if minx.y > points[i].y:
                minx = points[i]
                minind = i
    return minind

def rightmost(points,n): 
    # Returns index of the first rightmost and lowest point in points list
    minx = points[0]
    minind = 0
    for i in range(n):
        if minx.x < points[i].x:
            minx = points[i]
            minind = i
        elif minx.x == points[i].x:
            if minx.y > points[i].y:
                minx = points[i]
                minind = i
    return minind    
   
def pivot_partition(points,low,high,by="x"):
    # Set pivot elemnt and index.
    pi = low
    if by == "x":
        pivot = points[low].x  
    else:
        pivot = points[low].y  
    low = pi + 1    
    while True:
        # Find high less than pivot and low greater than pivot to swap
        if by == "x":
            while low <= high and points[high].x >= pivot:
                high = high - 1
            while low <= high and points[low].x <= pivot:
                low = low + 1
        else:
            while low <= high and points[high].y >= pivot:
                high = high - 1
            while low <= high and points[low].y <= pivot:
                low = low + 1 
        # Switch if low hasn't passed high
        if low <= high:
            points[low], points[high] = points[high], points[low]
        else:
            break
    # Swap pivot and high point after creating partition
    points[pi], points[high] = points[high], points[pi]
    return high

    
def quicksort(points,low,high,by): 
    if low < high: 
        pi = pivot_partition(points,low,high,by)   
        quicksort(points, low, pi-1, by) 
        quicksort(points, pi+1, high, by) 
    return points
        

def sort_xy(points,n):
    points = quicksort(points,0,n,by="x")
    # for each in points:
    #     print(each)
    for i in range(0,n):
        if points[i].x == points[i+1].x:
            samef = i
            for j in range(i+1,n+1):
                # print(i,j)
                # 4,5, 6
                if points[j].x == points[i].x:
                    samel = j
                else:
                    i = j
                    break
            # print(samef,samel)
            # print("it")
            points = quicksort(points,samef,samel,by="y")
    return points
            


# points = []
# points.append(Point(4, 3))
# points.append(Point(0, 9)) 
# points.append(Point(7, 2)) 
# points.append(Point(5, 3))
# points.append(Point(5, 2))
# points.append(Point(3,10))
# points.append(Point(3, 3))
# points.append(Point(3, 2))



# points = sort_xy(points,len(points)-1)



# # points = quicksort(points,0,len(points)-1,by="x")
# for i in points:
#     print(i)



    
    




# # quickSort(points,0,len(points)-1)

# # # pi = pivot_partition(points,0,len(points)-1)

# # print(pi)

# for each in points:
#     print(each)

# len(points)-1
