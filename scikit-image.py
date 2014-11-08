import matplotlib.pyplot as plt
import numpy as np
import cv2
import itertools

from skimage.feature import greycomatrix, greycoprops
from skimage.color import rgb2gray
from sklearn import datasets, cluster
from sklearn.feature_extraction.image import grid_to_graph

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

    print A
    cv2.polylines(img, [pts], True, (0,255,255))

    # Show image
    image_gray = rgb2gray(P)
    #print image_gray

    #result = greycomatrix(image_gray, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], levels=4)

digits = datasets.load_digits()
images = digits.images
X = np.reshape(images, (len(images), -1))
connectivity = grid_to_graph(*images[0].shape)

agglo = cluster.FeatureAgglomeration(connectivity=connectivity,
                                     n_clusters=32)

agglo.fit(X)
X_reduced = agglo.transform(X)

X_restored = agglo.inverse_transform(X_reduced)
images_restored = np.reshape(X_restored, images.shape)
plt.figure(1, figsize=(4, 3.5))
plt.clf()
plt.subplots_adjust(left=.01, right=.99, bottom=.01, top=.91)
for i in range(4):
    plt.subplot(3, 4, i + 1)
    plt.imshow(images[i], cmap=plt.cm.gray, vmax=16, interpolation='nearest')
    plt.xticks(())
    plt.yticks(())
    if i == 1:
        plt.title('Original data')
    plt.subplot(3, 4, 4 + i + 1)
    plt.imshow(images_restored[i], cmap=plt.cm.gray, vmax=16,
               interpolation='nearest')
    if i == 1:
        plt.title('Agglomerated data')
    plt.xticks(())
    plt.yticks(())

plt.subplot(3, 4, 10)
plt.imshow(np.reshape(agglo.labels_, images[0].shape),
           interpolation='nearest', cmap=plt.cm.spectral)
plt.xticks(())
plt.yticks(())
plt.title('Labels')
plt.show()

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