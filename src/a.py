#!/usr/bin/env python3
# coding: utf8
import numpy
from skimage.segmentation import flood_fill
ary = numpy.array(
    [0,0,1,0,
     0,0,1,0,
     0,0,1,1,
     0,0,0,0
    ]).reshape(4, 4)
print(ary)
print(flood_fill(ary, (0, 0), 9))
