#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import math3d
from pymycobot import MyCobot280 

# print(dir(math3d))
#vec = math3d.Vector()
#trans_matrix = [[1, 0, 0, 10], [0, 1, 0, 20], [0, 0, 1, 30]]
trans_matrix = [[math.cos(0.3), -math.sin(0.3), 0, 10],
                [math.sin(0.3), math.cos(0.3), 0, 20], [0, 0, 1, 30]]
trans = math3d.Transform(trans_matrix)


print(dir(trans))
print(trans.pos.x)
print(trans.pos.y)
print(trans.pos.z)
print(trans.matrix)
print(trans.array)
print(trans.orient)
print(trans.pose_vector)

rpy = trans.orient.to_euler('xyz')
print(rpy)


mycobot = MyCobot280("COM8", 115200)
print(mycobot.get_coords())