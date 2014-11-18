import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from scipy.cluster.vq import kmeans,vq
from scipy.spatial.distance import cdist

fileNum = '00'
dataDir = 'data/path-image-1' + str(fileNum) + '.tif/'
ftPath = dataDir + 'path-image-1' + str(fileNum) + '.seg.000000.000000.csv'

def load_data(fName = ftPath):
  fp = open(fName)
  XX = np.loadtxt(fp)
  fp.close()
  return XX

##### cluster data into K=1..10 clusters #####
#K, KM, centroids,D_k,cIdx,dist,avgWithinSS = kmeans.run_kmeans(X,10)
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
  return(fig,ax)

def plot_clusters(orig, pred, nx, ny, legend=True):
  data = orig
  ylabels = { 0:'Male life expectancy in yrs',1:'Female life expectancy in yrs',2:'Infant mortality, per 1000'}
  # plot data into three clusters based on value of c
  p0 = plt.plot(data[pred==0,nx],data[pred==0,ny],'ro',label='Underdeveloped')
  p2 = plt.plot(data[pred==2,nx],data[pred==2,ny],'go',label='Developing')
  p1 = plt.plot(data[pred==1,nx],data[pred==1,ny],'bo',label='Developed')

  lx = p1[0].axes.set_xlabel('Per Capita GDP in US$')
  ly = p1[0].axes.set_ylabel(ylabels[ny])
  tt= plt.title('UN countries Dataset, KMeans clustering with K=3')
  if legend:
    ll=plt.legend()
  plt.show()
  return (p0, p1, p2)


X = load_data(ftPath)
kIdx = 2
km = KMeans(kIdx, init='k-means++') # initialize
km.fit(X)
c = km.predict(X) # classify into three clusters

(pl0,pl1,pl2) = plot_clusters(X,c,3,2) # column 3 GDP, vs column 2 infant mortality. Note indexing is 0 based