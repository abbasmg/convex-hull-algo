import time, random
from Coord import Point
import matplotlib.pyplot as plt
import brute as b
import jarvis as j
import graham as g
import dandc as d


def random_points(points, n):
    randomx = []
    randomy = []
    for i in range(0, n):
        # any random numbers from 0 to 1000
        randomx.append(random.randint(0,100))
        randomy.append(random.randint(0,100))
        x,y = randomx[i], randomy[i]
        points.append(Point(x, y))


def time_complexity(k_brute, k_divide, k):
    times_brute = []
    times_divide = []
    times_jarvis = []
    times_graham = []
    n = []
    n_brute = []
    n_divide = []

    for i in range(5,k_brute,1):
        points = []
        n_brute.append(i)
        random_points(points, i)

        print("------")
        # Brute
        tic = time.perf_counter()
        b.convex_hull(points, len(points))
        toc = time.perf_counter()
        times_brute.append(toc-tic)
        print("------")
        
        print(i-4)

    for i in range(5,k_divide+5):
        points = []
        n_divide.append(i)
        random_points(points, i)

        print("------")
        # Divide and conquer
        tic = time.perf_counter()
        d.convex_hull(points,len(points),8)
        toc = time.perf_counter()
        times_divide.append(toc-tic)
        print("------")
        
        print(i-4)

    for i in range(5,k+5):
        points = []
        n.append(i)
        random_points(points, i)

        print("------")
        # Jarvis
        tic = time.perf_counter()
        j.convex_hull(points, len(points))
        toc = time.perf_counter()
        times_jarvis.append(toc-tic)

        # Graham O(nlogn)
        tic = time.perf_counter()
        g.convex_hull(points)
        toc = time.perf_counter()
        times_graham.append(toc-tic)
        print("------")
        
        print(i-4)
    
    return n_brute, n_divide, n, times_brute, times_divide, times_jarvis, times_graham



n_brute, n_divide, n, times_brute, times_divide, times_jarvis, times_graham = time_complexity(0,0,0)

# Plot brute algo ------------------
fig, ax = plt.subplots()
ax.plot(n_brute,times_brute)

ax.set(xlabel='No. of elements', ylabel='Time required',
       title='Brute algo time complexity')
ax.grid()

fig.savefig("brute.png")
plt.show()


# Plot Div&Conq algo ------------------
fig, ax = plt.subplots()
ax.plot(n_divide,times_divide)

ax.set(xlabel='No. of elements', ylabel='Time required',
       title='Divide and Conquer algo time complexity')
ax.grid()

fig.savefig("div&conq.png")
plt.show()


# Plot Jarvis algo ------------------
fig, ax = plt.subplots()
ax.plot(n,times_jarvis)

ax.set(xlabel='No. of elements', ylabel='Time required',
       title='Jarvis algo time complexity')
ax.grid()

fig.savefig("jarvis.png")
plt.show()


# Plot Graham algo ------------------
fig, ax = plt.subplots()
ax.plot(n,times_graham)

ax.set(xlabel='No. of elements', ylabel='Time required',
       title='Graham algo time complexity')
ax.grid()

fig.savefig("graham.png")
plt.show()



# Plot convex polygon ------------------
# this was manually done using the GUI
times_convexpoly =[
    0.005133,
    0.00858129999997459,
    0.008160400000008394,
    0.007028600000012375,
    0.011166000000002896,
    0.007819600000004812,
    0.015481300000033116,
    0.012539199999991979,
    0.017975700000022243,
    0.017781899999988582
]
n_convpoly = range(5,55,5)
fig, ax = plt.subplots()
ax.plot(n_convpoly,times_convexpoly)

ax.set(xlabel='No. of elements', ylabel='Time required',
       title='Convex hull of simple polygon time complexity')
ax.grid()

fig.savefig("convPoly.png")
plt.show()