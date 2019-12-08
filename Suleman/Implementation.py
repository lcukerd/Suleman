import sys

image = loadImage("test.png");
labels, avg_height, centroids, DemoImg, stats = findComponents(image);
linesO = findHoughLines(DemoImg, image, avg_height);

lines = np.copy(linesO);
selLines = [];
selStats = [];

dists = np.zeros((len(lines), len(centroids))) -1;
dists.shape

while (True):
    print (str(len(lines)) + " Lines left");
    (rho_, theta_), pos_ = findPrimaryCell(lines, centroids)

    f_clus = findClustersize(theta_, avg_height)
    print (f_clus);

    x0 = rho_ - f_clus
    x1 = rho_ + f_clus
    z0 = theta_ - math.radians(3)
    z1 = theta_ + math.radians(3)

    clusCells, clusPos, lines, stop = findcells(x0, x1, z0, z1, lines);
    if (stop):
        break;
    print (len(lines))
    print (len(clusCells));
    showLines(clusCells, DemoImg)
    n0 = findValueofcell([(rho_, theta_)], centroids, pos_)
    print (n0);

    ntemp = 0
    rho1, theta1 = 0,0
    lpos1 = 0;
    for pos in range(len(clusCells)):
        i = clusCells[pos];
        if (i[0][0] == rho_ and i[0][1] == theta_):
            continue
        temp = findValueofcell(i, centroids, pos)
        if (temp > ntemp):
            ntemp = temp
            rho1 = i[0][0]
            theta1 = i[0][1]
            lpos1 = clusPos[pos];

    (rhon, thetan) , pos = compareValueinStruct([(rho_, theta_)], pos_, [(rho1, theta1)], lpos1, centroids, x0, x1, z0, z1, n0, ntemp)

    print ((rhon, thetan));
    selLines.append((rhon, thetan));
    selStats.append(stats[pos])
    showLines([[(rhon, thetan)]], DemoImg);

dists.shape






# Image Validation

data = [];
validLines = [];
for line in selLines:
    lineData = [];
    x1, x2, y1, y2 = findLine(line[0][0], line[0][1])
    lineF = Line((x1,y1),(x2,y2));
    for i in range(len(selStats)):
        stat = selStats[i]:
        centroid = centroids[i];
        labelDataCont = [];
        labelDataNCont = [];
        x1, y1 = int (stat[0]), int (stat[1]);
        x2, y2 = int (stat[0]), int (stat[1] + stat[3]);
        x3, y3 = int (stat[0] + stat[2]), int (stat[1]);
        x4, y4 = int (stat[0] + stat[2]), int (stat[1] + stat[3]);

        segment1 = Segment((x1, y1), (x2, y2));
        segment2 = Segment((x2, y2), (x3, y3));
        segment3 = Segment((x3, y3), (x4, y4));
        segment4 = Segment((x4, y4), (x1, y1));

        i1 = lineF.intersection(segment1)
        i2 = lineF.intersection(segment2)
        i3 = lineF.intersection(segment3)
        i4 = lineF.intersection(segment4)

        # Only put if line intersects this component
        if (not (len(i1) == 0 and len(i2) == 0 and len(i3) == 0 and len(i4) == 0)):
            labelDataCont.append([stat]);
            labelDataCont.append([centroid]);
            labelDataCont.append([i1,i2,i3,i4]);
        else:
            labelDataNCont.append([stat]);
            labelDataNCont.append([centroid]);

    lineData.append(labelDataCont);
    lineData.append(labelDataNCont);
data.append(lineData);


for line in data:
    line[0] = sort (line[0]);
    if len(line[0]) > 2 :
        intNeigh = (len(line[0]) - 2) * 2 + 2;
    else:
        intNeigh = len(line[0]);
    extNeigh = 0;
    for i in range(1, len(line[0]) - 1):
        comp = line[0][i];
        extDistance = extDist(line, i);

        for stat in line[1]:

            dist = findDistanceBWcomp(comp[1], stat[1]);

            if (dist < extDistance):
                extNeigh += 1;
    if (extNeigh > intNeigh):
        validLines(line);










# How to choose:
# Threshold: number of points to fall on line before it is declared line
# Minimum length of line
# Maximum distanace between line

# How to validate a line
# Measuring nearest distance between centroid and line:
#     but how to decide what is the line set for choice
# If external neighbors is greater than the number of internal ones:
#     don't understand how this will work



## Test
a = np.array([[[5],[6],[1]],[[4],[7],[1]],[[3],[8],[1]],[[2],[9],[1]]])
ind = np.argsort(a, axis = 0)

np.take_along_axis(a, ind, axis=0)

showLines([[(0.0, 0)]], DemoImg);
