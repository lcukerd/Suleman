import math
import numpy as np
import globalVar

from sympy import Point, Polygon
from sympy.geometry import Segment, Line

def findDistance(x1, x2, x3, y1, y2, y3):
    line = Line((x1,y1), (x2,y2))
    point = Point (x3, y3)
    # if (distance[(line,point)] is null):
    #     distance[(line,point)] = line.distance(point)
    # return distance[(line,point)]
    return line.distance(point)

def findLine(rho, theta):
    a = math.cos(theta)
    b = math.sin(theta)
    x0 = a * rho
    y0 = b * rho

    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    return x1, x2, y1, y2

def findValueofcell(line, centroids, lpos):
    ntemp = 0

    x1, x2, y1, y2 = findLine(line[0][0], line[0][1])

    for i in range(len(centroids)):
        pt = centroids[i]
        x3 = int(pt[0])
        y3 = int(pt[1])
        if (globalVar.dists[lpos][i] == -1):
            dist = findDistance(x1, x2, x3, y1, y2, y3);
            globalVar.dists[lpos][i] = dist;
        else:
            dist = globalVar.dists[lpos][i];
        if (dist < 5):
            ntemp +=1
    return ntemp


def findClustersize(theta, avg_height):
    theta = math.degrees(theta)
    if (theta > 85 and theta < 95):
        return 5
    else:
        return 2.5

def findPointsofRect(rho0, rho1, theta0, theta1):

    c0 = math.cos(theta0)
    s0 = math.sin(theta0)

    c1 = math.cos(theta1)
    s1 = math.sin(theta1)

    x0 = round (c0 * rho0, 3)
    y0 = round (s0 * rho0, 3)

    x1 = round (c1 * rho0, 3)
    y1 = round (s1 * rho0, 3)

    x2 = round (c0 * rho1, 3)
    y2 = round (s0 * rho1, 3)

    x3 = round (c1 * rho1, 3)
    y3 = round (s1 * rho1, 3)

    return [(x0,y0), (x1,y1), (x2,y2), (x3,y3)]

def sort (line):
    ind = np.argsort([cont[0][0][0] for cont in line]);
    line = [line[i] for i in ind]

    return line

def larger(intersections):
    point = None
    temp = -10000

    for i in intersections:
        if (len(i) != 0):
            if (i[0].x > temp):
                temp = i[0].x;
                point = i[0];
    return point


def smaller(intersections):
    point = None
    temp = 10000

    for i in intersections:
        if (len(i) != 0):
            if (i[0].x < temp):
                temp = i[0].x;
                point = i[0];
    return point

# def extDistanceBWcomp(cent1, cent2):
#     # Edge to edge distance along line joining centroids

def findDistanceBWcomp(comp1, comp2):
    point1 = Point (int (comp1[0]), int (comp1[1]))
    point2 = Point (int (comp2[0]), int (comp2[1]))

    return int (point1.distance(point2));
