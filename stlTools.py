import struct
import time

'''
A pretty effiecient stl reader for python

Facet vertex count is default 3 but can be specified
'''
def readStl(stlFile_abspath,binary=True,vertexPerFacet=3):
    start = time.time()
    if binary:
        facets,vertexL = readBinary(stlFile_abspath,vertexPerFacet)
    else:
        facets,vertexL = readAscii(stlFile_abspath,vertexPerFacet)
    for i,f in enumerate(facets):
        print "N:",f
        print "V:",[v for v in vertexL[i*3:(i*3)+3]]    
    print "File import took: %s" %(time.time()-start)

def parseBinaryvertex(oFile):
    '''Read 3 floats from binary and unpack'''
    x,y,z = struct.unpack("fff",oFile.read(12))
    return (x,y,z)

def parseAsciiVertex(line):
    x,y,z = line.split()[1:]
    return (float(x),float(y),float(z))

def parseFacet(data,n):
    '''Read n lines of ascii, data is on line 0,2-(n+2)'''
    normal = data[0].split()[2:]
    vertex = [ parseAsciiVertex(d) for d in data[2:n+2] ]
    return normal,vertex
    
def readBinary(stlFile_abspath,n):
    '''read a binary stl, n is number of vertices per face'''
    facets = []
    vertexL = []
    oFile = open(stlFile_abspath,'rb')
    header = oFile.read(80)
    numFacets = struct.unpack("i",oFile.read(4))[0]
    
    for i in range(numFacets):
        normal = parseBinaryvertex(oFile)
        vertex = [ parseBinaryvertex(oFile) for i in range(n) ]
        endData = oFile.read(2)
        facets.append(normal)
        for v in vertex: vertexL.append(v) 
    oFile.close()
    return facets,vertexL

def readAscii(stlFile_abspath,n):
    '''read an ascii stl, n is number of vertices per face'''
    facets = []
    vertexL = []
    with open(stlFile_abspath,'r') as oFile:
        header = oFile.readline().split()[0]
        data = True
        while data: #Read the facets
            data = [ oFile.readline() for i in range(n) ]
            if '' not in data:
                normal,vertex = parseFacet(data,n)
                facets.append(normal)
                for v in vertex: vertexL.append(v) 
            else:
                data = False
    oFile.close()
    return facets,vertexL
