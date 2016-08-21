import bpy
from bpy import context
import os
import sys
import time
import mathutils

ob = bpy.data.objects["Object"]
mesh = ob.data

# Extend sword
for vert in mesh.vertices:
	new_location = vert.co
	new_location[1] = new_location[1] * 2
	new_location[2] = new_location[2] * 2
	vert.co = new_location

highest = -9999999

for vert in mesh.vertices:
	new_location = vert.co
	if (new_location[2] > highest):
		highest = new_location[2]

for vert in mesh.vertices:
	new_location = vert.co
	new_location[2] = new_location[2] - highest
	vert.co = new_location
