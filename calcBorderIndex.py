import matplotlib.pyplot as plt
import numpy as np
import cv2
import itertools
import math
import os

from skimage.feature import greycomatrix, greycoprops
from skimage.color import rgb2gray
from PIL import Image
#from skimage import data, util
#from skimage.morphology import label

def pairwise(iterable):
    "s -> (s0,s1), (s2,s3), (s4, s5), ..."
    a = iter(iterable)
    return itertools.izip(a, a)
	
#Calc_PeriFunction
def calc_peri(coords):
    Nedges = len(coords)-1
    length = []
    for i in xrange(Nedges):
        ax, ay = coords[i]
        bx, by = coords[i+1]
        #print ax,ay
        length.append(math.hypot(bx-ax, by-ay))
    #print length

    peri_poly = np.sum(length)
    return peri_poly 

#BoudaryIndexFunction
def bounding_index(coords):
    min_x = 100000 # start with something much higher than expected min
    min_y = 100000
    max_x = -100000 # start with something much lower than expected max
    max_y = -100000
	
    for item in coords:
      if item[0] < min_x:
        min_x = item[0]
		
      if item[0] > max_x:
        max_x = item[0]

      if item[1] < min_y:
        min_y = item[1]

      if item[1] > max_y:
        max_y = item[1]
      
    Nedges = len(coords)-1
    length = []
    for i in xrange(Nedges):
        ax, ay = coords[i]
        bx, by = coords[i+1]
        #print ax,ay
        length.append(math.hypot(bx-ax, by-ay))
    #print length
    
    peri_poly = np.sum(length)
    peri_rect =2*(math.hypot(min_x - max_x, min_y - min_y) + math.hypot(max_x - max_x, min_y - max_y))
    #print "peri_poly",peri_poly
    #print "peri_rect",peri_rect 

    return peri_poly/peri_rect		

#BoundingBoxCoord
def bounding_box(coords):
    min_x = 100000 # start with something much higher than expected min
    min_y = 100000
    max_x = -100000 # start with something much lower than expected max
    max_y = -100000

    for item in coords:
      if item[0] < min_x:
        min_x = item[0]

      if item[0] > max_x:
        max_x = item[0]

      if item[1] < min_y:
        min_y = item[1]

      if item[1] > max_y:
        max_y = item[1]

    Nedges = len(coords)-1
    length = []
    for i in xrange(Nedges):
        ax, ay = coords[i]
        bx, by = coords[i+1]
        length.append(math.hypot(bx-ax, by-ay))

    #return [(min_x,min_y),(max_x,min_y),(max_x,max_y),(min_x,max_y)]
    return (min_x,min_y,min_x+(max_x-min_x),min_y+(max_y-min_y))


#Variance
def variance(list):
   average = sum(list) / len(list)
   var=0
   for i in list:
        var += math.pow((average - i),2)
        
    #    print var
   return var/len(list)



# Load path-image from .jpg
imgPath = 'path-image-100.000000.000000.jpg'
#NamedWindow("opencv")
img = cv2.imread(imgPath)

# Load polygons co-ordinates from .txt
txtPath = 'path-image-100.seg.000000.000000.txt'
txt = open(txtPath, 'r')

# Write features in csv
ftPath = 'hackrpi/features.csv'
ft = open(ftPath, 'w')

# Convert polygons to numpy array
numPoly = []
t=1
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

    #1.Area calculation
    a = x[:-1] * y[1:]
    b = y[:-1] * x[1:]
    Area = np.sum(a - b) / 2
    
    #5 BoundaryIndex
    BoundaryIndex = bounding_index(polygon)
    #print "Bounding Index: " + str(BoundaryIndex)
    #for x1,y1 in polygon:
    # print x1,y1

    #BoundingBox
    im = Image.open(imgPath) #the size is 500x350 
    box = bounding_box(polygon)
    #print "box", box
    kay = im.crop(box)
    kay.save("poly_images/polygon" + str(t) + ".jpeg")
    t+=1
 
    #2.Perimeter
    perimeter= calc_peri(polygon)
    #print "perimeter:",perimeter
    
    #3.Compactness
    compactness= Area/(perimeter*perimeter)
    #print compactness

    #4.Asymetry
    xy = x * y
    #print "var(x)", variance(x)
    #print "var(y)", variance(y)
    #print "var(xy)", variance(xy)
    assym = (2*math.sqrt((0.25*((variance(x)+variance(y))**2))+variance(xy)-(variance(x)*variance(y))))/(variance(x)+variance(y))
    #print assym 
    
    
    ft.write(str(Area) + ' ' + str(perimeter) + ' ' + str(compactness) + ' ' + str(assym) + ' '+ str(BoundaryIndex)+ '\n')
    
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
