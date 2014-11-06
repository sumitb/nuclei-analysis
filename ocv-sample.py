import numpy as np
import cv2
import itertools

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
    cv2.polylines(img, [pts], True, (0,255,255))

# Show image
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
