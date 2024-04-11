import numpy
from random import random
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import cv2

def heatmap(anum2):
    plt.ion()
    colors = [(20/255, 252/255, 3/255), (252/255, 186/255, 3/255), (1, 0, 0)]  # Green, Yellow, Red
    cmap = LinearSegmentedColormap.from_list('CustomMap', colors)

    plt.clf()
    hm = numpy.empty([720,1280], dtype=float)

    for i in range (720):
        for j in range(1280):
            if anum2[i][j]==1:
                rl = i-100 if i-100>=0 else 0
                ru = i+100 if i+100<720 else 719
                cl = j-100 if j-100>=0 else 0
                cu = j+100 if j+100<1280 else 1219
                asub = anum2[rl:ru, cl:cu]
                unique, counts = numpy.unique(asub, return_counts=True)
                num = dict(zip(unique, counts))
                num.setdefault(1, 0)
                if num[1]>1:
                    for x in range (rl,ru):
                        for y in range (cl,cu):
                            hm[x][y] = 1
                rl = i-70 if i-70>=0 else 0
                ru = i+70 if i+70<720 else 719
                cl = j-70 if j-70>=0 else 0
                cu = j+70 if j+70<1280 else 1219
                asub = anum2[rl:ru, cl:cu]
                unique, counts = numpy.unique(asub, return_counts=True)
                num = dict(zip(unique, counts))
                num.setdefault(1, 0)
                if num[1]>1:
                    for x in range (rl,ru):
                        for y in range (cl,cu):
                            hm[x][y] = 2

    for i in range (720):
        for j in range (1280):
            if hm[i][j] not in (1,2):
                hm[i][j] = 0
    print(hm)

    hm_blurred = cv2.GaussianBlur(hm.astype(float), (249, 249), 0)
    
    plt.imshow(hm_blurred, cmap=cmap, interpolation='gaussian')
    plt.colorbar(ticks=[0, 1, 2], label='Value').set_ticklabels(['Safe', 'Warning', 'Violation'])
    plt.draw()
