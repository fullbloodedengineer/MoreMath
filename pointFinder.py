#!/usr/bin/env python
import numpy
import random
from scipy.spatial import KDTree
import time

class Tree:
    '''Create a KDTree from a defined set of points, KDTree is not designed to be
        updated. We build the tree once and can quickly find items. 
    '''
    def __init__(self,pts):
        self.a = numpy.array(pts)
        self.tree = KDTree(self.a, leafsize=10)#smaller leaf size takes longer to build but faster to search

    def find_pts(self,test_pt,search_radius):
        distances, ndx = self.tree.query(test_pts, k=5, distance_upper_bound=search_radius)
        #print distances[0]
        #print ndx[0]
        allIndex = []
        for dist in distances:
            index_list = [ndx[0][i] for i,d in enumerate(dist) if d != numpy.inf]
            allIndex.append(index_list)
        return allIndex

    def findRandom(self,search_radius):
        pt = create_random_point()
        indexes = tree.find_pts(pt,search_radius)
        for i in indexes:
            print "Found %s within range" %(len(i))
              
def create_points(count):
    data = []
    for _ in xrange(count):
        data.append(create_random_point())
    return data

def create_random_point():
    return [ random.randrange(10000) for _ in range(3) ]    

if __name__ == "__main__":
    pts = create_points(10**6)
    tree = Tree(pts)

    test_pts = create_points(1000)
    sT = time.time()
    #for i in xrange(1000000): tree.findRandom(100)

    #Testing all points at once completes in 0.8seconds
    indexes = tree.find_pts(test_pts,100)
    fT = time.time()
    for i in indexes:
            print "Found %s within range" %(len(i))
    print "Completed in",fT-sT
