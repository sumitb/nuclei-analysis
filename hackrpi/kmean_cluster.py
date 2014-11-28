import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from scipy.cluster.vq import kmeans,vq
from scipy.spatial.distance import cdist
from os import getcwd
fileNum = '00'
#dataDir = 'data/path-image-1' + str(fileNum) + '.tif/'
#ftPath = dataDir + 'path-image-1' + str(fileNum) + '.seg.000000.000000.csv'
dataDir = getcwd() + '/../data/path-image-1' + str(fileNum) + '.tif/'

def load_data(fi):
  fName = dataDir + fi
  fp = open(fName)
  XX = np.loadtxt(fp)
  fp.close()
  return XX

def run_kmeans(X, n=10):
  _K = range(1, n)

  # scipy.cluster.vq.kmeans
  _KM = [kmeans(X,k) for k in _K] # apply kmeans 1 to 10
  _centroids = [cent for (cent,var) in _KM]   # cluster centroids

  _D_k = [cdist(X, cent, 'euclidean') for cent in _centroids]

  _cIdx = [np.argmin(D,axis=1) for D in _D_k]
  _dist = [np.min(D,axis=1) for D in _D_k]
  _avgWithinSS = [sum(d)/X.shape[0] for d in _dist]

  return (_K, _KM, _centroids, _D_k, _cIdx, _dist, _avgWithinSS)

def plot_elbow_curve(kIdx, K, avgWithinSS):
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.plot(K, avgWithinSS, 'b*-')
  ax.plot(K[kIdx], avgWithinSS[kIdx], marker='o', markersize=12,
      markeredgewidth=2, markeredgecolor='r', markerfacecolor='None')
  plt.grid(True)
  plt.xlabel('Number of clusters')
  plt.ylabel('Average within-cluster sum of squares')
  tt = plt.title('Elbow for KMeans clustering')
  plt.show()
  #return(fig,ax)
#/////////////////////////////////////////////////////////////////////////////////

def plot_clusters(orig, pred, nx, ny, fo, legend=True):
  data = orig
  ylabels = { 0:'',1:'',2:''}
  # plot data into three clusters based on value of c
  p0 = plt.plot(data[pred==0,nx],data[pred==0,ny],'ro',label='Cluster 1')
  p2 = plt.plot(data[pred==2,nx],data[pred==2,ny],'go',label='Cluster 2')
  p1 = plt.plot(data[pred==1,nx],data[pred==1,ny],'bo',label='Cluster 3')
  lx = p1[0].axes.set_xlabel('')
  ly = p1[0].axes.set_ylabel(ylabels[ny])
  tt= plt.title('Polygon Dataset, KMeans clustering with K=3')
  plt.xlabel('Area of polygons')
  plt.ylabel('Perimeter of polygons')
 
  if legend:
    ll=plt.legend()
  plt.savefig(dataDir + "kmeans/" + fo)
  plt.show()
  plt.clf()
  return (p0, p1, p2)

def start_kmeans(fi,fo):
  X = load_data(fi)
  kIdx = 3
  km = KMeans(kIdx, init='k-means++') # initialize
  km.fit(X)
  c = km.predict(X) # classify into three clusters
  
  (pl0,pl1,pl2) = plot_clusters(X,c,0,1,fo) # column 0 AREA, vs column 1 Perimeter . Note indexing is 0 based
#for testing
#start_kmeans("path-image-100.seg.000000.000000.csv","myfilter_test.png")
##### cluster data into K=1..10 clusters #####
"""X = load_data("filterFeature.csv")
K, KM, centroids,D_k,cIdx,dist,avgWithinSS = run_kmeans(X,10)
print cIdx
kIdx =2
plot_elbow_curve(kIdx, K, avgWithinSS)"""
