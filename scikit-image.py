import matplotlib.pyplot as plt
import numpy as np
import cv2
import itertools

from skimage.feature import greycomatrix, greycoprops
from skimage.color import rgb2gray

def pairwise(iterable):
    "s -> (s0,s1), (s2,s3), (s4, s5), ..."
    a = iter(iterable)
    return itertools.izip(a, a)

# Load path-image from .jpg
imgPath = 'path-image-100.000000.000000.jpg'
#NamedWindow("opencv")
img = cv2.imread(imgPath)

# Load polygons co-ordinates from .txt
txtPath = 'path-image-100.seg.000000.000000.txt'
txt = open(txtPath, 'r')

# Write features in csv
ftPath = 'features.csv'
ft = open(ftPath, 'w')

# Convert polygons to numpy array
numPoly = []
for poly in txt:
    polygon = []
    polyList = poly.split(',')
    while '' in polyList:
        polyList.remove('')
    if '\n' in polyList:
        polyList.remove('\n')
    for i, num in enumerate(polyList):
        polyList[i] = int(polyList[i])

    #x1, y1 = polyList[0], polyList[1]

    # Draw a line from every co-ordinate with thickness of 1 px
    for x, y in pairwise(polyList):
        polygon.append([x, y])
    pts = np.array(polygon, np.int32)
    pts = pts.reshape((-1,1,2))
    numPoly.append(pts)

    # feature 1: Area
    P = np.array(polygon)
    # Extract x and y coordinates
    x = P[:, 0]
    y = P[:, 1]

    # Area calculation
    a = x[:-1] * y[1:]
    b = y[:-1] * x[1:]
    A = np.sum(a - b) / 2.
    #A = int(A)

    ft.write(str(A) + ' ' + str(A/2) + ' ' + str(2*A) + ' ' + str(3*A) +'\n')
    cv2.polylines(img, [pts], True, (0,255,255))

    # Show image
    image_gray = rgb2gray(P)
    #print image_gray

    #result = greycomatrix(image_gray, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], levels=4)

'''
# create the figure
fig = plt.figure(figsize=(8, 8))

# display original image with locations of patches
ax = fig.add_subplot(1, 1, 1)
ax.imshow(image_gray, interpolation='nearest',
          vmin=0, vmax=255)

# display the patches and plot
fig.suptitle('Grey level co-occurrence matrix features', fontsize=14)
plt.show(fig)
'''