import bpy
import bmesh
from math import sqrt, atan2, atan, sin, cos
import mathutils

obj = bpy.data.objects["Guard.002"]

mesh = obj.data

radiusOut = 2
radiusIn = 4
for vert in mesh.vertices:
    newV = vert.co
    
    alpha = atan2(newV[2], newV[1])
    oldRadius = sqrt(pow(newV[1],2) + pow(newV[2],2))

    realOld = oldRadius
    fakeNew = (10-newV[0])*(abs(radiusOut-radiusIn)/10)
    fakeOld = (10-newV[0])/5
    realNew = realOld * fakeNew / fakeOld
    h = realNew

    newV[1] = h * cos(alpha)
    newV[2] = h * sin(alpha)
    
    vert.co = newV