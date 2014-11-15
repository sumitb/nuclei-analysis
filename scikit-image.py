import matplotlib.pyplot as plt
import numpy as np
import itertools

from skimage.io import *
from skimage.draw import polygon
from skimage.feature import greycomatrix, greycoprops
from skimage.color import rgb2gray
from skimage.measure import label, regionprops

def pairwise(iterable):
    "s -> (s0,s1), (s2,s3), (s4, s5), ..."
    a = iter(iterable)
    return itertools.izip(a, a)

# Load path-image from .jpg
imgPath = 'path-image-100.000000.000000.jpg'
#NamedWindow("opencv")
#img = cv2.imread(imgPath)
img = imread(imgPath) #set as_grey=True for grayscale

# Crop to remove black
img = img[:1870, :2340]
lx, ly, rgbval = img.shape

# Load polygons co-ordinates from .txt
txtPath = 'path-image-100.seg.000000.000000.txt'
txt = open(txtPath, 'r')

# Write features in csv
ftPath = 'features.csv'
ft = open(ftPath, 'w')

# Convert polygons to numpy array
count = 0
numPoly = []

for poly in txt:
    polyX = []
    polyY = []
    polygn = []

    polyList = poly.split(',')
    polyImg = np.zeros((lx, ly), dtype=np.uint8)
    while '' in polyList:
        polyList.remove('')
    if '\n' in polyList:
        polyList.remove('\n')
    for i, num in enumerate(polyList):
        polyList[i] = int(polyList[i])

    for x, y in pairwise(polyList):
        polyX.append(x)
        polyY.append(y)
        polygn.append([x, y])

    #print type(polygn), polygn
    # Extract x and y coordinates
    x = np.array(polyX)
    y = np.array(polyY)
    rr, cc = polygon(y, x)
    polyImg[rr, cc] = False
    mask = np.array(polyImg)
    img[mask] = 0
    print mask
    plt.imshow(img, interpolation='nearest', vmin=0, vmax=255)

    '''
    pts = np.array(polygn, np.int32)
    pts = pts.reshape((-1,1,2))
    numPoly.append(pts)
    '''

    # feature 1: Area calculation
    a = x[:-1] * y[1:]
    b = y[:-1] * x[1:]
    A = np.sum(a - b) / 2.

    ft.write(str(A) + ' ' + str(A/2) + ' ' + str(2*A) + ' ' + str(3*A) +'\n')
    # Draw a line from every co-ordinate with thickness of 1 px
    #cv2.polylines(img, [pts], True, (0,255,255))

    # feature 2: Bounding Index
    #label_img = label(P)
    #regions = regionprops(label_img)

    # feature 3: Compute luminance of an RGB image.
    #img_gray = rgb2gray(img)

    #result = greycomatrix(image_gray, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], levels=4)
    count = count + 1
    if count > 3:
        break


# create the figure
plt.figure(figsize=(8, 8))
plt.imshow(img, interpolation='nearest', vmin=0, vmax=255)
plt.show()