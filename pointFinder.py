#!/usr/bin/env python
import numpy
import random
from scipy.spatial import KDTree
import timeit,cProfile
import functools

class Tree:
    def __init__(self,pts):
        self.a = numpy.array(pts)
        self.tree = KDTree(self.a, leafsize=10)#smaller leaf size takes longer to build but faster to search

    def find_pts(self,test_pt,search_radius):
        distances, ndx = self.tree.query([test_pt], k=5, distance_upper_bound=search_radius)
        #print distances[0] #We only tested one point so its a single array
        #print ndx[0]
        index_list = [ndx[0][i] for i,d in enumerate(distances[0]) if d != numpy.inf]
        return index_list

    def findRandom(self,search_radius):
        pt = create_random_point()
        indexes = tree.find_pts(pt,search_radius)
        print "Found %s within range" %(len(indexes))
        #for index in indexes:
        #    print self.a[index]
              
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
    for i in xrange(100): tree.findRandom(100)
