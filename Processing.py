from sympy import Point, Polygon
from sympy.geometry import Segment, Line
from GeometryProcessing import *

def findPrimaryCell(lines, centroids):
    n = 0
    lineP = (0,0);
    pos = 0;
    for i in range(len(lines)):
        line = lines[i]
        if (line[0][0] == 0 and line[0][1] == 0):
            continue;
        ntemp = findValueofcell(line, centroids, i)
        if (ntemp > n):
            lineP = line
            n = ntemp
            pos = i;
    return lineP[0], pos

def findcells(x0, x1, z0, z1, lines):
    clusCells = []
    clusPos = []
    nonClusCells = []
    stop = True;

    vertices = findPointsofRect(x0, x1, z0, z1);

    segment1 = Segment(vertices[0], vertices[1]);
    segment2 = Segment(vertices[1], vertices[3]);
    segment3 = Segment(vertices[3], vertices[2]);
    segment4 = Segment(vertices[2], vertices[0]);

    for i in range(len(lines)):
        line = lines[i];
        if (line[0][0] == 0 and line[0][1] == 0):
            nonClusCells.append([(0,0)])
            continue;
        x1, x2, y1, y2 = findLine(line[0][0], line[0][1])
        lineF = Line((x1,y1),(x2,y2))

        i1 = lineF.intersection(segment1)
        i2 = lineF.intersection(segment2)
        i3 = lineF.intersection(segment3)
        i4 = lineF.intersection(segment4)

        if (not (len(i1) == 0 and len(i2) == 0 and len(i3) == 0 and len(i4) == 0)):
            clusCells.append(line)
            clusPos.append(i);
            nonClusCells.append([(0,0)])
            stop = False;
        else:
            nonClusCells.append(line)

    return clusCells, clusPos, np.array(nonClusCells), stop, vertices


def compareValueinStruct(cell0, lpos0, cell1, lpos1, centroids, x0, x1, z0, z1, n0, n1):
    vertices = findPointsofRect(x0, x1, z0, z1);

    rect = Polygon(vertices[0], vertices[1], vertices[3], vertices[2])
    points = [];

    for point in centroids:
        if (rect.encloses_point(point)):
            points.append(point)

    cell0V = findValueofcell(cell0, points, lpos0)
    cell1V = findValueofcell(cell1, points, lpos1)

    if ((n1/n0)>0.65 and cell1V>cell0V):
        return cell1[0] , lpos1
    else:
        return cell0[0] , lpos0

def extDist(line, i):
    compL = line[i-1];
    isL = larger(compL[2]);

    compM = line[i];
    isML = smaller(compM[2]);
    isMR = larger(compM[2]);

    compR = line[i-1];
    isR = smaller(compR[2]);

    return (isL.distance(isML) + isMR.distance(isR))/2;
