import numpy as np

class vertex:
    def __init__(self,loc):
        self.uid = 1
        if type(loc,list) and len(loc) == 3:
            self.pos = np.array(loc)
        else:
            #TODO Raise error for invalid type cast
            pass

    def __eq__(self, other): 
        return self.pos == other.pos

    def distanceToVertex(self, other):
        return numpy.linalg.norm(self.pos-other.pos)

class edge:
    def __init__(self,vertexA, vertexB):
        self.vertexA = vertexA
        self.vertexB = vertexB

    def __eq__(self, other):
        A = (self.vertexA == other.vertexA) or (self.vertexA == other.vertexB)
        B = (self.vertexB == other.vertexA) or (self.vertexB == other.vertexB)
        return (A and B)

    def vertexInEdge(self,vertex):
        AB = self.vertexA.distanceToVertex(self.vertexB)
        AV = self.vertexA.distanceToVertex(vertex)
        VB = vertex.distanceToVertex(self.vertexB)

class orderEdgeLoop:
    def __init__(self,edgeLoop=[]):
        self.edgeLoop = edgeLoop
        if not isLoop:
            self.edgeLoop = []
            #TODO raise error for invalid loop
        
    def insertEdgeIntoLoop(self,edge,after=None)
        '''Given an edge, index to insert after'''        
        v1N = edge.vertexA
        v2N = edge.vertexB
        if not after == None or not before == None:
            if (
                    v1N == self.edgeLoop[after].vertexB and 
                    v2N == self.edgeLoop[before].vertexA
                ):
                #Inser edge into loop
                self.edgeLoop.insert(edge,after)
   
    def isLoop(self):
        '''Verify that the loop is valid'''
        for i,edge in enumerate(self.edgeLooap):
            vEnd = edge.vertexA
            vNext = edge[self.wrapAround(i,1)].vertexA
            if not vEnd == vNext:
                return False       
        return True
            
                        
    def wrapAroundIndex(self,i,loc):
        return (i+loc) % len(self.edgeLoop)

class face:
    def __init__(self,edgeLoop=None,name=None):
        self.uid = 1
        self.name = name
        self.edgeLoop = edgeLoop

    def teselateFace(self):
        pass

class mesh:
    def __init__(self,name):
        self.name = name

    def addFace(self):
        pass

    def ifClosed(self):
        return True

    def findVolume(self):
        if isClosed():
            return 9000.0