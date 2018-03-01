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
        return numpself.pos == other.pos

    def coincident(self, other, tol=1e-2):
        test = np.isClose(self.pos,other.pos,rtol=tol)
        return (test[0] and test[0])

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

    def vertexInEdge(self,vertex,tol=0.01):
        AB = self.vertexA.distanceToVertex(self.vertexB)
        AV = self.vertexA.distanceToVertex(vertex)
        VB = vertex.distanceToVertex(self.vertexB)

        return (AB + tol >= AV + VB) and (AB - tol <= AV + AB)

    @static
    def perpendicular(a):
        b = np.empty_like(a)
        b[0] = -a[1]
        b[1] = a[0]
        return b

    def intersectEdge(self,other):
        da = self.vertexB-self.vertexA
        db = other.vertexB-other.vertexA
        dp = self.vertexA - other.vertexA
        dap = self.perpendicular(a)
        denom = np.dot(dap,db)
        if denom 
        num = np.dot(dap,dp)
        return (num / denom.astype(float))*db + other.vertexA

class orderEdgeLoop:
    def __init__(self,edgeLoop=[]):
        self.edgeLoop = edgeLoop
        self.valid = self.isLoop()
        
    def insertEdgeAfterIndex(self,edge,after=None)
        '''Given an edge, index to insert after'''        
        v1N = edge.vertexA
        v2N = edge.vertexB
        if not after == None:
            nextIndex = self.wrapAroundIndex(after,1)
            if (
                    v1N == self.edgeLoop[after].vertexB and 
                    v2N == self.edgeLoop[nextIndex].vertexA
                ):
                #Insert edge into loop
                self.edgeLoop.insert(edge,after)
   
    def isLoop(self):
        '''Verify that the loop is valid'''
        if len(self.edgeLoop) == 0:
            return False
        else:
            for i,edge in enumerate(self.edgeLooap):
                vEnd = edge.vertexA
                vNext = edge[self.wrapAroundIndex(i,1)].vertexA
                if not vEnd == vNext:
                    return False       
            return True

    def findEdge(self,edge):
        for i,_edge in enumerate(self.edgeLoop):
            if _edge == edge:
                return i
        return None
            
    def next(self,edge):
        for i,_edge in enumerate(self.edgeLoop):
            if _edge == edge:
                return wrapAroundIndex(i,1)
        return None
                        
    def wrapAroundIndex(self,i,loc):
        return (i+loc) % len(self.edgeLoop)

class face:
    '''A face'''
    def __init__(self,edgeLoop=None,name=None):
        self.uid = 1
        self.name = name
        self.edgeLoop = edgeLoop

    def teselateFace(self):
        pass

    def normal(self):
        return np.array([1,0,0])

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