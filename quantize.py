# -*- coding: utf-8 -*-
"""
Created on Sun May  2 13:43:53 2021

@author: Allegra Copland
"""
import matplotlib.pyplot as plt
from skimage import data,color
import numpy as np
astro = data.astronaut()
from utility import get_blocks,grid_im,LOCAL_IMAGE
from dct_grid import dct_on_grid,dct2


ycbcr = color.rgb2ycbcr(LOCAL_IMAGE)
blocks = [get_blocks(ycbcr[:,:,i]) for i in range(3)]
grid_im(blocks[0],cmap=plt.cm.gray)
grid_im(dct_on_grid(blocks[0]),cmap=plt.cm.gray)