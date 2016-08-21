import bpy
from bpy import context
import os
import sys
import time

argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"

ob = bpy.data.objects["Object"]
mesh = ob.data

#root_dir = os.path.dirname(os.path.realpath(__file__))
#filepath = os.path.join(root_dir, 'generated', 'model' + '_' + str(int(time.time())) + '.obj')

filepath = argv[0]
print('DEBUG ' + argv[1])
length = int(argv[1])

# Extend sword
for vert in mesh.vertices:
	new_location = vert.co
	if new_location[0] > 0:
		new_location[0] = new_location[0] + length #X
		#new_location[1] = new_location[1] + 1 #Y
		#new_location[2] = new_location[2] + 1 #Z
		vert.co = new_location

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