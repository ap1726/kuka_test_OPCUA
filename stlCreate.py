import numpy as np
from stl import mesh
import math

def getNearIndex(arrayList, startIndex, steps):
    length = len(arrayList)
    if (startIndex) >= (length-steps):
        index = 99
    else:
        index = startIndex+steps
    # if (startIndex) >= length-1:
    #     index = 80
    return int(index)
# ================== CIRCLE ==================
circleTest = {}
circleTest["x"] = []
circleTest["y"] = []
circleTest["z"] = []
radius=1
x0=0
y0=0
z0=0
fi = []
tetha = []
arrayTriangles=[]
verticlesNumberArray=[]
arrayVertices=[]
steps=10
for j in range(steps):
    fi.append(j*2*math.pi/steps)
    tetha.append(j*math.pi/steps)
for i in range(len(tetha)*len(fi)):
    verticlesNumberArray.append(i)
for j in range(len(tetha)):
    for i in range(len(fi)):
        x=x0+radius*math.sin(tetha[j])*math.cos(fi[i])
        y=y0+radius*math.sin(tetha[j])*math.sin(fi[i])
        z=z0+radius*math.cos(tetha[j])

        circleTest["x"].append(x)
        circleTest["y"].append(y)
        circleTest["z"].append(z)
for ax in range(len(circleTest["x"])):
    arrayVertices.append([circleTest["x"][ax],circleTest["y"][ax],circleTest["z"][ax]])
vertices = np.array(arrayVertices)
# Define the X triangles composing the circle
for k in range(len(tetha)*len(fi)):
    first = verticlesNumberArray[getNearIndex(verticlesNumberArray, k, steps)]
    second = verticlesNumberArray[getNearIndex(verticlesNumberArray, k-1, steps)]
    arrayTriangles.append([k,first,second])
print(arrayTriangles)
faces = np.array(arrayTriangles)
# /================= END CIRCLE ==================


outputSTLobject = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        outputSTLobject.vectors[i][j] = vertices[f[j],:]

# Write the mesh to file "cube.stl"
outputSTLobject.save('cube.stl')
