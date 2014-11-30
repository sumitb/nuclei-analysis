import kmean_cluster as mykc

mykc.start_kmeans("area100.csv","area100.png",[0,0])
mykc.start_kmeans("boundaryIndex.csv","boundaryIndex.png",[4,4])
mykc.start_kmeans("path-image-100.seg.000000.000000.csv","allFeatures.png",[0,1])
mykc.start_kmeans("area_homogenity.csv","area_homogenity.png",[0,7])
mykc.start_kmeans("compactness_correlation.csv","compactness_correlation.png",[2,8])
mykc.start_kmeans("permimeter_dissimilarity.csv","permimeter_dissimilarity.png",[1,9])

