from kmean_cluster import main
from plot_dbscan import start_dbscan

#Cluster based on filters
def filteredCluster(paraList):

    fileNum = '00'
    dataDir = '../data/path-image-1' + str(fileNum) + '.tif/'
    ftPath = dataDir + 'path-image-1' + str(fileNum) + '.seg.000000.000000.csv'
    fp = open(ftPath,'r')
    filterFeature = dataDir+'filterFeature.csv' 
    fw = open(filterFeature,'w')
    
    data = fp.readlines()
    for i,para in enumerate(paraList):
        #print f
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
    i = 0
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
        i +=1
        if i >1000:
            break
        """print area
        print perimeter
        print compactness
        print assym
        print BoundaryIndex
        print contrast
        print energy
        print homogeneity
        print correlation
        print dissimilarity
        print correlation
        print dissimilarity
        print asm"""
        
        if ((area >filter_area[0] and area <filter_area[1]) or
            (perimeter >filter_perimeter[0] and perimeter <filter_perimeter[1]) or
            (compactness >filter_compactness[0] and compactness <filter_compactness[1]) or
            (assym >filter_assym[0] and assym <filter_assym[1]) or
            (BoundaryIndex >filter_BoundaryIndex[0] and BoundaryIndex >filter_BoundaryIndex[1]) or
            (contrast >filter_contrast[0] and contrast <filter_contrast[1]) or
            (energy >filter_energy[0] and energy <filter_energy[1]) or
            (homogeneity >filter_homogeneity[0] and homogeneity <filter_homogeneity[1]) or
            (correlation >filter_correlation[0] and correlation <filter_correlation[1]) or
            (dissimilarity >filter_dissimilarity[0] and dissimilarity <filter_dissimilarity[1])or
            (asm >filter_asm[0] and asm <filter_asm[1]) ):
          
          print "found"
          fw.write(str(area)+ " "+str(perimeter)+ " "+str(compactness)+ " "+str(assym)+ " "+
            str(BoundaryIndex)+ " "+str(contrast)+ " "+str(energy)+ " "+str(homogeneity)+ " "+
            str(correlation)+ " "+str(dissimilarity)+ "\n")
        else:
            print("not found")

    main("filterFeature.csv","myfeature.png")
    start_dbscan("filterFeature.csv","myfeature_dbscan.png")
        #print paraList
    """for para in paraList:
            print para
            if para[0]=='area':
                min = para[1]
                max = para[2]
                #print Area 
                if( Area >min and Area < max):
                    myquery += str(Area) + " "
                else:
                    myquery = None
                    break
                    
            elif para[0]=='perimeter':
                min = para[1]
                max = para[2]
                print perimeter
                if( perimeter >min and perimeter < max):
                    myquery += str(perimeter) + " "
                else:
                    myquery = None
                    break
            elif para[0]=='compactness':
                min = para[1]
                max = para[2]
                if( compactness >min and compactness < max):
                    myquery += str(compactness) + " "
                else:
                    myquery = None
                    break
            elif para[0]=='assym':
                min = para[1]
                max = para[2]
                if( assym >min and assym < max):
                    myquery += str(assym) + " "
                else:
                    myquery = None
                    break
            elif para[0]=='BoundaryIndex':
                min = para[1]
                max = para[2]
                if( BoundaryIndex >min and BoundaryIndex < max):
                    myquery += str(BoundaryIndex) + " "
                else:
                    myquery = None
                    break
            elif para[0]=='contrast':
                min = para[1]
                max = para[2]
                if( contrast >min and contrast < max):
                    myquery += str(contrast) + " "
                else:
                    myquery = None
                    break
            elif para[0]=='energy':
                min = para[1]
                max = para[2]
                if( energy >min and energy < max):
                    myquery += str(energy) + " "
                else:
                    myquery = None
                    break
            elif para[0]=='homogeneity':
                min = para[1]
                max = para[2]
                if( homogeneity >min and homogeneity < max):
                    myquery += str(homogeneity) + " "
                else:
                    myquery = None
                    break
            elif para[0]=='correlation':
                min = para[1]
                max = para[2]
                if( correlation >min and correlation < max):
                    myquery += str(correlation) + " "
                else:
                    myquery = None
                    break
            elif para[0]=='dissimilarity':
                min = para[1]
                max = para[2]
                i= f( dissimilarity >min and dissimilarity < max):
                    myquery += str(dissimilarity) + " "
                else:
                    myquery = None
                    break
            elif para[0]=='asm':
                min = para[1]
                max = para[2]
                if( ASM >min and ASM < max):
                    myquery += str(ASM) + " "
                else:
                    myquery = None
                    break
        if myquery:
            print("writing data: "+myquery)
        #fw.write(myquery+"\n")"""

#for testing only comment in real code
"""area =[0.0,250.0]
peri = [0.0,250.0]
compactness = [0.0,150.0]
assym =[0.0,150.0]
BoundaryIndex=[0.0,150.0]
contrast=[0.0,150.0]
energy=[0.0,150.0]
homogeneity=[0.0,150.0]
correlation=[0.0,150.0]
dissimilarity=[0.0,150.0]
assym=[0.0,150.0]
filteredCluster(area,peri,compactness,assym,BoundaryIndex,contrast,energy,
    homogeneity,correlation,dissimilarity,assym)"""