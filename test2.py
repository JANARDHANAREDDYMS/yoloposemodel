import numpy
from random import random
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

plt.ion()
colors = [(40/255, 252/255, 3/255), (252/255, 186/255, 3/255), (1, 0, 0)]  # Green, Yellow, Red
cmap = LinearSegmentedColormap.from_list('CustomMap', colors)
for q in range(1000):
    plt.clf()
    anum = numpy.random.choice([0, 1], size=100, p=[.90, .1])
    anum2 = numpy.empty([10,10], dtype=int)
    hm = numpy.empty([10,10], dtype=int)
    count = 0
    for i in range(10):
        for j in range(10): 
            anum2[i][j] = anum[count]
            count+=1
    print(anum2)
    for i in range (10):
        for j in range(10):
            if anum2[i][j]==1:
                rl = i-2 if i-2>=0 else 0
                ru = i+2 if i+2<10 else 9
                cl = j-2 if j-2>=0 else 0
                cu = j+2 if j+2<10 else 9
                asub = anum2[rl:ru, cl:cu]
                unique, counts = numpy.unique(asub, return_counts=True)
                num = dict(zip(unique, counts))
                num.setdefault(1, 0)
                if num[1]>1:
                    for x in range (rl,ru):
                        for y in range (cl,cu):
                            hm[x][y] = 1
                rl = i-1 if i-1>=0 else 0
                ru = i+1 if i+1<10 else 9
                cl = j-1 if j-1>=0 else 0
                cu = j+1 if j+1<10 else 9
                asub = anum2[rl:ru, cl:cu]
                unique, counts = numpy.unique(asub, return_counts=True)
                num = dict(zip(unique, counts))
                num.setdefault(1, 0)
                if num[1]>1:
                    for x in range (rl,ru):
                        for y in range (cl,cu):
                            hm[x][y] = 2

    for i in range (10):
        for j in range (10):
            if hm[i][j] not in (1,2):
                hm[i][j] = 0
    print(hm)

    plt.imshow(hm,cmap=cmap, interpolation='gaussian')
    plt.colorbar(ticks=[0, 1, 2], label='Value').set_ticklabels(['Safe', 'Warning', 'Violation'])
    plt.draw()
    plt.pause(0.1)

plt.ioff()