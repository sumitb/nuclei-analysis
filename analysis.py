import matplotlib.pyplot as plt
import numpy as np
import itertools
import math
import os

from skimage.io import *
from skimage.draw import polygon
from skimage.feature import greycomatrix, greycoprops
from skimage.color import rgb2gray
from skimage.measure import label, regionprops
from PIL import Image, ImageDraw


fileNum = '00'
dataDir = 'data/path-image-1' + str(fileNum) + '.tif/'



def pairwise(iterable):
    "s -> (s0,s1), (s2,s3), (s4, s5), ..."
    a = iter(iterable)
    return itertools.izip(a, a)


#Calculate Perimeter Function
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

#Cluster based on filters
def filteredCluster(f):
	fp = open(f,'r')
	fw1 = open(dataDir+'area100.csv','w')
	fw2 = open(dataDir+'compactness_correlation.csv','w')
	fw3 = open(dataDir+'area_homogenity.csv','w')
	fw4 = open(dataDir+'permimeter_dissimilarity.csv','w')
	fw5 = open(dataDir+'boundaryIndex.csv','w')
	i=0
	data = fp.readlines()
    	for line in data:
                i = i+1
                print (i)
                value = line.split()
                Area = float(value[0])
                perimeter = float(value[1])
                compactness = float(value[2])
                assym = float(value[3])
                BoundaryIndex = float(value[4])
		contrast = float(value[5])
		energy = float(value[6])
		homogeneity = float(value[7])
		correlation = float(value[8])
		dissimilarity = float(value[9])
		ASM = float(value[10])
                # filter 1: area > 100
                if Area > 100:
			fw1.write(str(Area) + ' ' + str(perimeter) + ' ' + str(compactness) + ' ' + str(assym) + ' '+str(BoundaryIndex)+ ' '+
        str(contrast) + ' '+  str(energy)+ ' '  +  str(homogeneity)+ ' '  + str(correlation)+ ' '  + str(dissimilarity)+ ' '  + str(ASM)+"\n")
	
		# filter 2: compactness 0.02-0.05 and correlation > 0.8 
		if compactness > 0.02 and compactness < 0.05 and correlation > 0.8: 
			fw2.write(str(Area) + ' ' + str(perimeter) + ' ' + str(compactness) + ' ' + str(assym) + ' '+str(BoundaryIndex)+ ' '+
        str(contrast) + ' '+  str(energy)+ ' '  +  str(homogeneity)+ ' '  + str(correlation)+ ' '  + str(dissimilarity)+ ' '  + str(ASM)+"\n")
		
		# filter 3: area > 150 and homogenityi > 0.999998
		if Area > 150 and homogeneity > 0.999998:
			fw3.write(str(Area) + ' ' + str(perimeter) + ' ' + str(compactness) + ' ' + str(assym) + ' '+str(BoundaryIndex)+ ' '+
        str(contrast) + ' '+  str(energy)+ ' '  +  str(homogeneity)+ ' '  + str(correlation)+ ' '  + str(dissimilarity)+ ' '  + str(ASM)+"\n")

		#filter 4: perimeter < 45 and dissimilarity > 0.0004
		if perimeter < 45 and dissimilarity > 0.0004:
			fw4.write(str(Area) + ' ' + str(perimeter) + ' ' + str(compactness) + ' ' + str(assym) + ' '+str(BoundaryIndex)+ ' '+
        str(contrast) + ' '+  str(energy)+ ' '  +  str(homogeneity)+ ' '  + str(correlation)+ ' '  + str(dissimilarity)+ ' '  + str(ASM)+"\n") 
		
		#filter 5: boundaryIndex = 1
		if BoundaryIndex == 1:
			fw5.write(str(Area) + ' ' + str(perimeter) + ' ' + str(compactness) + ' ' + str(assym) + ' '+str(BoundaryIndex)+ ' '+
        str(contrast) + ' '+  str(energy)+ ' '  +  str(homogeneity)+ ' '  + str(correlation)+ ' '  + str(dissimilarity)+ ' '  + str(ASM)+"\n")

ftPath = dataDir + 'path-image-1' + str(fileNum) + '.seg.000000.000000.csv'


fileNum = '05'
dataDir = 'data/path-image-1' + str(fileNum) + '.tif/'

# Load path-image from .jpg
imgPath = dataDir + 'path-image-1' + str(fileNum) + '.000000.000000.jpg'

# Load polygons co-ordinates from .txt
txtPath = dataDir + 'path-image-1' + str(fileNum) + '.seg.000000.000000.txt'
txt = open(txtPath, 'r')

# Write features in csv
ftPath = dataDir + 'path-image-1' + str(fileNum) + '.seg.000000.000000.csv'
ft = open(ftPath, 'w')

img = imread(imgPath) #set as_grey=True for grayscale
# Crop to remove black
img = img[:1870, :2340]
lx, ly, rgbval = img.shape
    
# read image as RGB and add alpha (transparency)
im = Image.open(imgPath).convert("L")
# convert to numpy (for convenience)
imArray = np.asarray(im)

with open(txtPath, 'r') as fin:
    data = fin.read().splitlines(True)
with open(txtPath, 'w') as fout:
    fout.writelines(data[1:])

numPoly = []
polyId = 1

# Convert polygons to numpy array
for line in txt:
    poly = line.split('\t')
    poly = poly[51:]
    poly = poly[0]
    poly = poly.replace(';', ',')

    mypoly = []
    polyList = poly.split(',')
    while '' in polyList:
        polyList.remove('')
    if '\n' in polyList:
        polyList.remove('\n')
    for i, num in enumerate(polyList):
        polyList[i] = int(float(polyList[i]))


    #x1, y1 = polyList[0], polyList[1]

    # Draw a line from every co-ordinate with thickness of 1 px
    for x, y in pairwise(polyList):
        mypoly.append((x, y))
        #polyX.append(x)
        #polyY.append(y)
        
    #pts = np.array(mypoly, np.int32)
    #pts = pts.reshape((-1,1,2))
    
    #numPoly.append(pts)

    P = np.array(mypoly)
    # Extract x and y coordinates
    x = P[:, 0]
    y = P[:, 1]

    #1.Area calculation
    a = x[:-1] * y[1:]
    b = y[:-1] * x[1:]
    Area = np.sum(a - b) / 2
    
    #5 BoundaryIndex
    BoundaryIndex = bounding_index(mypoly)
    #print "Bounding Index: " + str(BoundaryIndex)
    #for x1,y1 in polygon:
    # print x1,y1

    #BoundingBox
    #im = Image.open(imgPath) #the size is 500x350
    box = bounding_box(mypoly)
    #print "box", box
    #key = im.crop(box)
    #key.save("poly_images/polygon" + str(polyId) + ".jpg")
    polyId += 1
 
    #2.Perimeter
    perimeter= calc_peri(mypoly)
    #print "perimeter:",perimeter
    
    #3.Compactness
    compactness= Area/(perimeter*perimeter)
    #print compactness

    #4.Assymetry
    xy = x * y
    #print "var(x)", variance(x)
    #print "var(y)", variance(y)
    #print "var(xy)", variance(xy)
    assym = (2*math.sqrt((0.25*((variance(x)+variance(y))**2))+variance(xy)-(variance(x)*variance(y))))/(variance(x)+variance(y))
    #print assym 
    
    #///////////////////////////////////////////////////////////////////////////////////////////////////
    #GraylevelCocurrenceMatrix
    # create mask
    maskIm = Image.new('L', (imArray.shape[1], imArray.shape[0]), 0)
    ImageDraw.Draw(maskIm).polygon(mypoly, outline=1, fill=1)
    mask = np.array(maskIm)

    # assemble new image (uint8: 0-255)
    newImArray = np.empty(imArray.shape,dtype='uint8')

    # colors (three first columns, RGB)
    newImArray[:,:] = imArray[:,:]

    # transparency (4th column)
    newImArray[:,:] = mask*255
    
    newIm = Image.fromarray(newImArray, "L")#.convert("L")
    #newIm.save("out"+str(count)+".png")  

    #image_file = Image.open("out"+str(count)+".png").convert("L") # open colour image  
    #image_file = image_file.convert('1') # convert image to black and white
    #glcm = greycomatrix(np.asarray(newIm), [1], [0], 256, symmetric=True, normed=True)
    glcm = greycomatrix(np.asarray(newIm), [1], [0], 256, symmetric=True, normed=True)

    contrast = greycoprops(glcm, 'contrast').item()
    energy = greycoprops(glcm, 'energy').item()
    homogeneity = greycoprops(glcm, 'homogeneity').item()
    #print('homogeneity is: ',  homogeneity)
    correlation = greycoprops(glcm, 'correlation').item()
    #print('correlation is: ',  correlation)
    dissimilarity = greycoprops(glcm, 'dissimilarity').item()
    #print('dissimilarity is: ',  dissimilarity)
    ASM = greycoprops(glcm, 'ASM').item()
    #print('ASM is: ',  ASM)


    #/////////////////////////////////////////////////////////////////////////////////////
    ft.write(str(Area) + ' ' + str(perimeter) + ' ' + str(compactness) + ' ' + str(assym) + ' '+str(BoundaryIndex)+ ' '+
        str(contrast) + ' '+  str(energy)+ ' '  +  str(homogeneity)+ ' '  + str(correlation)+ ' '  + str(dissimilarity)+ ' '  + str(ASM)+"\n")

    #/////////////////////////////////////////////////////////////////////////////////////

filteredCluster(ftPath)
