# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:10:26 2020

@author: abbme
"""

from tkinter import *
from Coord import *
import jarvis as j
import graham as g
import brute as b
import dandc as d
import poly as p
import random
import time

    
points = []
lines = []
canvas = None
frame = None
height = 600
width = 1000

def callback(event):
    x, y = event.x, event.y
    points.append(Point(x, (height-y)))
    canvas.create_rectangle(x-1, y-1, x + 1, y + 1, fill="#6F0D5F")

# def insert_manual_point(x,y):
#     points.append(Point(x,y))
#     canvas.create_rectangle(x-1, y-1, x + 1, y + 1, fill="#6F0D5F")
    
# Clears everything
def clear_canvas(e):
    canvas.delete("all")
    points.clear()
    lines.clear()

# Clears lines from the gui so we can try other algorithms
def clear_lines(e):
    canvas.delete("line")
    lines.clear()

# Generates 100 random points for each button click
def random_points(e):
    randomx = []
    randomy = []
    for i in range(0, 100):
        # any random numbers from 0 to 1000
        randomx.append(random.randint(100,width-100))
        randomy.append(random.randint(100,height-100))
        x,y = randomx[i], randomy[i]
        points.append(Point(x, height-y))
        canvas.create_rectangle(x-1, y-1, x + 1, y + 1, fill="#6F0D5F")

# Brute force method for convex hull    
def brute(e):
    if display_error() == "er":
        clear_canvas(e)
        raise Exception("Error")
    h1,h2 = b.convex_hull(points, len(points))
    n = len(h1)
    for i in range(n):
        canvas.create_line(points[h1[i]].x,height - points[h1[i]].y, points[h2[i]].x,height - points[h2[i]].y, tag ="line")

# Jarvis method of convex hull    
def jarvis(e):
    if display_error() == "er":
        clear_canvas(e)
        raise Exception("Error")   
    hull = j.convex_hull(points, len(points))
    # Created two more list to improve readability
    hx = []
    hy = []
    for each in hull:
        hx.append(points[each].x)
        hy.append(height-points[each].y)
    n = len(hx)
    for i in range(n):
        canvas.create_line(hx[i%n], hy[i%n], hx[(i+1)%n], hy[(i+1)%n], tag ="line")
        
# Graham method of convex hull    
def graham(e):
    if display_error() == "er":
        clear_canvas(e)
        raise Exception("Error")   
    hull = g.convex_hull(points)
    # Created two more list to improve readability
    hx = []
    hy = []
    for each, point in enumerate(hull):
        hx.append(point.x)
        hy.append(height-point.y)
    n = len(hx)
    for i in range(n):
        canvas.create_line(hx[i%n], hy[i%n], hx[(i+1)%n], hy[(i+1)%n], tag ="line")
        
        
def divide(e):
    hulls,time1 = d.convex_hull(points,len(points),8)
    #print(hulls)
    if (hulls=="Error"):
        MsgBox = messagebox.showerror("Error", "Put atleast 3 points")
        return "er"
    for every in hulls:
        hx = []
        hy = []
        for each in every:
            hx.append(each.x)
            hy.append(height-each.y)
        n = len(hx)
        for i in range(n):
            canvas.create_line(hx[i%n], hy[i%n], hx[(i+1)%n], hy[(i+1)%n], tag ="line",fill = "red")
    #ul,ur,ll,lr = d.mergec(hulls)
    newhull, time2 = d.conquer(hulls)
    print("Processing time for D&C convex hull: " + str(time1+time2) + " seconds")
    nhx = []
    nhy = []
    for j,l in enumerate(newhull):
        for i in l:
            nhx.append(i.x)
            nhy.append(height-i.y)
    n = len(nhx)
    for i in range(n):
        canvas.create_line(nhx[i%n], nhy[i%n], nhx[(i+1)%n], nhy[(i+1)%n], tag ="line")
    # canvas.create_line(ul.x, height-ul.y, ur.x, height-ur.y, tag ="line",fill = "blue")
    # canvas.create_line(ll.x, height-ll.y, lr.x, height-lr.y, tag ="line",fill= "blue")
   
def polygon(e):
    q = p.convex_poly(points)        
                         
    hx = []
    hy = []
    for each in q:
        hx.append(each.x)
        hy.append(height-each.y)
    n = len(hx)
    for i in range(n):
        canvas.create_line(hx[i%n], hy[i%n], hx[(i+1)%n], hy[(i+1)%n], tag ="line")
    hpx = []
    hpy = []
    for each in points:
        hpx.append(each.x)
        hpy.append(height-each.y)
    n = len(hpx)
    for i in range(n):
        canvas.create_line(hpx[i%n], hpy[i%n], hpx[(i+1)%n], hpy[(i+1)%n], tag ="line", fill="red")
 

# To be used when we implement the preprossesing step of creating
# convex quadrilateral and deleting points within. Not done yet
def del_points(e):
     if display_error() == "er":
        clear_canvas(e)
        raise Exception("Error")

# To be used for the divide and conquer method of convex hull. Not done yet
def sort_points(e):
    sort_xy(points,len(points)-1)

# display error if less than 3 points
def display_error():
   if (len(points)<3):
        MsgBox = messagebox.showerror("Error", "Put atleast 3 points")
        return "er"

# Display coordinates of all the points being used
def display_points(e):
    for each in points:
        print(each)


root = Tk()     
   
frame = Frame(root, bg='grey', height=2)
frame.pack()

canvas = Canvas(frame, width=width, height=height)
canvas.pack(fill=BOTH, expand=1)
canvas.bind('<Button-1>', callback)

pbutton = Button(frame, text="Gen-points")
pbutton.pack(side='left', padx=10)
pbutton.bind('<Button-1>', random_points)

sbutton = Button(frame, text="sort_points")
sbutton.pack(side='left', padx=10)
sbutton.bind('<Button-1>', sort_points)

bbutton = Button(frame, text="Brute")
bbutton.pack(side='left', padx=10)
bbutton.bind('<Button-1>', brute)

jbutton = Button(frame, text="Jarvis")
jbutton.pack(side='left', padx=10)
jbutton.bind('<Button-1>', jarvis)

gbutton = Button(frame, text="Graham")
gbutton.pack(side='left', padx=10)
gbutton.bind('<Button-1>', graham)

dcbutton = Button(frame, text="D&C")
dcbutton.pack(side='left', padx=10)
dcbutton.bind('<Button-1>', divide)

cpbutton = Button(frame, text="C-Polygon")
cpbutton.pack(side='left', padx=10)
cpbutton.bind('<Button-1>', polygon)

clearlines = Button(frame, text = "c-lines")
clearlines.pack(side = 'left', padx=10)
clearlines.bind('<Button-1>', clear_lines)

clear = Button(frame, text="clear")
clear.pack(side='left', padx=10)
clear.bind('<Button-1>', clear_canvas)

dbutton = Button(frame, text="display_points")
dbutton.pack(side='left', padx=10)
dbutton.bind('<Button-1>', display_points)

frame.mainloop()

# insert_manual_point(445,102)
# insert_manual_point(445,110)