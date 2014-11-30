import os
#Cluster based on filters
fileNum = '00'
curDir = os.path.dirname(os.path.realpath("__file__"))
parDir = os.path.abspath(os.path.join(curDir, os.pardir))  #abspath(curDir/..)
dataDir = parDir + '/data/path-image-1' + str(fileNum) + '.tif/'
ftPath = dataDir + 'path-image-1' + str(fileNum) + '.seg.000000.000000.csv'

def filteredCluster(paraList):

    fp = open(ftPath,'r')
    fName = dataDir+'filterFeature.csv' 
    fw = open(fName,'w')
    featureIndexList = []
    data = fp.readlines()
    for i,para in enumerate(paraList):
        if(para !=None):
            featureIndexList.append(i)
        
    
    for line in data:
        value = line.split()
        area = float(value[0])
        perimeter = float(value[1])
        compactness = float(value[2])
        assym = float(value[3])
        BoundaryIndex = float(value[4])
        contrast = float(value[5])
        energy = float(value[6])
        homogeneity = float(value[7])
        correlation = float(value[8])
        dissimilarity = float(value[9])
        asm = float(value[10])
        
        feature = ""
        for i,index in enumerate(featureIndexList):
            para = paraList[index]
            
            if (float(value[index])>=para[0]) and (float(value[index]) <= para[1]):
                feature += str(float(value[index])) + " "
                #print "check here"            
            else:
                feature = ""
                break
        
        if(feature != ""):
            #print "found"
            fw.write(feature + "\n")
        else:
            pass
            #print("not found")
        
    #filteredCluster(0)
    fw.close()
    from kmean_cluster import start_kmeans
    from plot_dbscan import start_dbscan
    start_kmeans("filterFeature.csv","filterFeature.png",featureIndexList)
    start_dbscan("filterFeature.csv","filterFeature.png",featureIndexList)

#for testing
#paraList = [[0,100],[0,100],[0,100],[0,100],None,None,None,None,None,None,None,None]
#filteredCluster(paraList)