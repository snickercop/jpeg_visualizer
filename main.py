# -*- coding: utf-8 -*-
"""
Created on Tue May  4 15:47:34 2021

@author: Legs
"""

import numpy as np
from matplotlib import pyplot as plt
from dct_grid import dct_on_grid, bases_grid
from utility import LOCAL_IMAGE, get_blocks, grid_im
from color_transform import plot_rgb

grid = bases_grid()
#grid_im(grid) # outputs dct coefficient grid
x = 4
y = 4
q = 64 #size of the partition in pixels
image = LOCAL_IMAGE[(q*x):(q*(x+1)),(q*y):(q*(y+1))]
blocks = [get_blocks(image[:,:,i], dtype='uint8') for i in range(3)]
malformed_grid = [grid_im(blocks[i], recal=False, dtype='uint8', show=False) for i in range(3)] # needs to be reshaped in next line
malformed_grid = np.rot90(malformed_grid,1,(0,2))
plot_rgb(np.rot90(malformed_grid,3,(0,1)))
dctonblocks = dct_on_grid(blocks[0])
grid_im(dctonblocks, cmap=plt.cm.gray, title="%dx%d block at (%d,%d)"%(q, q, x, y))