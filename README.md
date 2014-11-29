nuclei-analysis
===============

a hadoop-gis project for data analytics.

Problem Statement:
Given set of Si of polygons (nuclei), compute feature vectors Fi from Pathology images.  Be creative about choice of features.  Examples

a) Mask area, perimeter,  shape
b) Within-mask texture
c) Padded region texture

Develop an interactive program that supports the following:

1) Select subset of features
2) Select number of clusters
3) Choose initial cluster centroids by random choice of data points 
4) Invoke  Kmeans clustering algorithm to cluster feature vectors 
5) Display clusters generated by clustering algorithm, cluster centroids along with within-cluster sum of squares 
6) Store clusters from Si : assignment of data points to clusters, initial cluster centroids, within-cluster sum of squares,  feature subset in database and all other metadata needed to re-run computation

TODO:
  A. UI Features
    i. Move to proper cluster section from nav menu
    ii. Pick a single query dropodown and place it properly
    iii. Remove dummy images from work and put workflow images
    iv. Display polygons in a info section from cluster
    v. Custom query option redesign and work with actual data
  B. Back-end
    i. Run whole slide images
    ii. Figure out how to use cluster power
    iii. Use mongo-db to prepopulate tables
    iv. Fix bug to populate clusters from predefined queries
