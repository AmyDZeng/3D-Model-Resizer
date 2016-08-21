import bpy
import bmesh
from math import sqrt, atan2, atan, sin, cos
import sys
import mathutils
import time


argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"

#ob = bpy.data.objects["Object"]
#mesh = ob.data

#root_dir = os.path.dirname(os.path.realpath(__file__))
#filepath = os.path.join(root_dir, 'generated', 'model' + '_' + str(int(time.time())) + '.obj')

filepath = argv[0]

obj = bpy.data.objects["Guard"]

mesh = obj.data

radiusWrist = 2
radiusForearm = 4
for vert in mesh.vertices:
	newV = vert.co

	alpha = atan2(newV[2], newV[1])
	oldRadius = sqrt(pow(newV[1],2) + pow(newV[2],2))

	realOld = oldRadius
	fakeNew = (10-newV[0])*(abs(radiusWrist-radiusForearm)/10)
	fakeOld = (10-newV[0])/5
	realNew = realOld * fakeNew / fakeOld
	h = realNew

	newV[1] = h * cos(alpha)
	newV[2] = h * sin(alpha)
    
	vert.co = newV

# Export as OBJ
with open(filepath, 'w') as f:
	f.write("# OBJ file\n")
	for v in mesh.vertices:
		f.write("v %.4f %.4f %.4f\n" % v.co[:])
	for p in mesh.polygons:
		f.write("f")
		for i in p.vertices:
			f.write(" %d" % (i + 1))
		f.write("\n")