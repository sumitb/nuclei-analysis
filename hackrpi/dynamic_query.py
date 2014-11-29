from os import getcwd
#Cluster based on filters
fileNum = '00'
dataDir = getcwd() + '/../data/path-image-1' + str(fileNum) + '.tif/'
ftPath = dataDir + 'path-image-1' + str(fileNum) + '.seg.000000.000000.csv'
    
def filteredCluster(paraList):

    fp = open(ftPath,'r')
    filterFeature = dataDir+'filterFeature.csv' 
    fw = open(filterFeature,'w')
    
    data = fp.readlines()
    for i,para in enumerate(paraList):
        if i == 0:
            filter_area = para
        if i == 1:
            filter_perimeter = para
        if i == 2:
            filter_compactness = para
        if i == 3:
            filter_assym = para
        if i == 4:
            filter_BoundaryIndex = para
        if i == 5:
            filter_contrat = para
        if i == 6:
            filter_energy = para
        if i == 7:
            filter_homogeneity= para
        if i == 8:
            filter_correlation = para
        if i == 9:
            filter_dissimilarity = para
        if i == 10:
            filter_asm = para
    #myquery = ""
    print "read start"
    #i = 0
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
        #i +=1
        #if i >1000:
            #break
        feature = ""
        if(filter_area and (area >=filter_area[0] and area <filter_area[1])):
            feature += str(area) + " "
      
        if(filter_perimeter and (perimeter >=filter_perimeter[0] and perimeter <filter_perimeter[1])):
            feature += str(perimeter) + " "

        if(filter_compactness and (compactness >=filter_compactness[0] and compactness <filter_compactness[1])):
            feature += str(compactness) + " "

        if(filter_assym and (assym >=filter_assym[0] and assym <filter_assym[1])):
            feature += str(assym) + " "
        
        if(filter_BoundaryIndex and (BoundaryIndex >=filter_BoundaryIndex[0] and BoundaryIndex >filter_BoundaryIndex[1])):
            feature += str(BoundaryIndex) + " "

        if(filter_contrast and (contrast >=filter_contrast[0] and contrast <filter_contrast[1])):
            feature += str(contrast) + " "
        
        if(filter_energy and (energy >=filter_energy[0] and energy <filter_energy[1])):
            feature += str(energy) + " "
        
        if(filter_homogeneity and (homogeneity >=filter_homogeneity[0] and homogeneity <filter_homogeneity[1])):
            feature += str(homogeneity) + " "
        
        if(filter_correlation and (correlation >=filter_correlation[0] and correlation <filter_correlation[1])):
            feature += str(correlation) + " "
        
        if(filter_dissimilarity and (dissimilarity >=filter_dissimilarity[0] and dissimilarity <filter_dissimilarity[1])):
            feature += str(dissimilarity) + " "
        
        if(filter_asm and (asm >=filter_asm[0] and asm <filter_asm[1])):
            feature += str(asm) + " "
        
        if(feature != ""):
            print "found"
            fw.write(feature + "\n")
        else:
            print("not found")

    #filteredCluster(0)
    from kmean_cluster import start_kmeans
    from plot_dbscan import start_dbscan
    start_kmeans("filterFeature.csv","filterFeature.png")
    start_dbscan("filterFeature.csv","filterFeature.png")