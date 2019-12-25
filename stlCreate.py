import numpy as np
from stl import mesh
import math

def getMirrorIndexOfArray(arrayList, startIndex):
    length = len(arrayList)
    if (startIndex+length/2) > length-1:
        index = startIndex+length/2-length
    else:
        index = startIndex+length/2
    return int(index)
# ================== CIRCLE ==================
circleTest = {}
circleTest["x"] = []
circleTest["y"] = []
circleTest["z"] = []
radius=1
x0=0
y0=0
fi = []
arrayTriangles=[]
verticlesNumberArray=[]
arrayVertices=[]
steps=50
for j in range(steps):
    fi.append(j*2*math.pi/steps)
    verticlesNumberArray.append(j)
for i in range(len(fi)):
    x=x0+radius*math.cos(fi[i])
    y=y0+radius*math.sin(fi[i])
    z=10
    circleTest["x"].append(x)
    circleTest["y"].append(y)
    circleTest["z"].append(z)

for ax in range(len(circleTest["x"])):
    arrayVertices.append([circleTest["x"][ax],circleTest["y"][ax],circleTest["z"][ax]])
vertices = np.array(arrayVertices)
# Define the X triangles composing the circle
for k in range(len(verticlesNumberArray)):
    first = verticlesNumberArray[getMirrorIndexOfArray(verticlesNumberArray, k)]
    second = verticlesNumberArray[getMirrorIndexOfArray(verticlesNumberArray, k-1)]
    arrayTriangles.append([k,first,second])
faces = np.array(arrayTriangles)
# /================= END CIRCLE ==================
# ================== CUBE ==================
# Define the 8 vertices of the cube
# vertices = np.array([\
#     [+0, +1, +0],
#     [+0.7, +0.7, +0],
#     [+1, +0, +0],
#     [+0.7, -0.7, +0],
#     [+0, -1, +0],
#     [-0.7, -0.7, +0],
#     [-1, +0, +0],
#     [-0.7, +0.7, +0]])
# Define the X vertices of the circle
# Define the 12 triangles composing the cube
# faces = np.array([\
#     [0,4,3],
#     [1,5,4],
#     [2,6,5],
#     [3,7,6],
#     [4,0,7],
#     [5,1,0],
#     [6,2,1],
#     [7,3,2]])
# Create the mesh
# /================== END CUBE ==================

outputSTLobject = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        outputSTLobject.vectors[i][j] = vertices[f[j],:]

# Write the mesh to file "cube.stl"
outputSTLobject.save('cube.stl')
