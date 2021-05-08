# -*- coding: utf-8 -*-
"""
Created on Tue May  4 15:47:34 2021

@author: Legs
"""

import numpy as np
from matplotlib import pyplot as plt
from dct_grid import dct_on_grid, bases_grid, dct2, idct2
from utility import LOCAL_IMAGE, get_blocks, grid_im, recalibrate,contrast_boost, binim
from color_transform import plot_rgb, plot_ycbcr
from downsample import compress_ycbcr as colorsquash
from skimage import color
from quantize import qmatrix, quantize

COLOR_REDUCTION = 4 # color downsampling factor

grid = bases_grid()
#grid_im(grid) # outputs dct coefficient grid

myimage = LOCAL_IMAGE
gray = (color.rgb2gray(LOCAL_IMAGE)*255).astype('int16')

# color transform and downsampling
rgb, ycbcr = colorsquash(myimage, COLOR_REDUCTION)

class ImPipeline(): # this holds all of the steps along the encoding "pipeline"
    def __init__(self,image):
        self.original = image
        self.steps = [0]*6
        self.display = [0]*6
        # blocking:
        self.blocks = get_blocks(image)
        self.steps[0] = self.blocks
        self.display[0] = self.blocks
        self.focus = (0,0) # you can select one block to look at closely when using show_step_focus
        # dct:
        self.blocks = dct_on_grid(self.blocks) # returns to range 0-255
        self.steps[1] = self.blocks
        self.display[1] = self.blocks.astype('uint8')+128
        # quantization:
        
    def show_step(self,i,contrast=True):
        a = self.steps[i]
        if contrast:
            a = contrast_boost(a)
        return grid_im(a, show=True, cmap=plt.cm.gray)
    
    def step_focus(self,i):
        return self.steps[i][self.focus[0]][self.focus[1]]
    
    def show_step_focus(self,i):
        out = self.display[i][self.focus[0]][self.focus[1]]
        plt.imshow(out, cmap=plt.cm.gray)
        return self.step_focus(i)
    
    def block(self,i,j):
        return self.blocks[i,j]
    
    def set_focus(self,i,j):
        self.focus = (i,j)
        return "Set new focus block to %d, %d" % (i,j)
    
    def get_focus(self):
        print("Current focus is %d, %d"%(self.focus[0],self.focus[1]))
        return self.blocks[self.focus[0]][self.focus[1]]
        
    def show_focus_context(self,i=0): # need to fix
        temp = grid_im(self.steps[i]).astype("int8")
        for x in range(self.focus[0]*9, self.focus[0]*9+10):
            for y in [self.focus[1]*9, self.focus[1]*9+10]:
                temp[x][y] = 255
        plt.imshow(temp,cmap=plt.cm.gray)
        
    # def quantize(self,k):
    #     self.steps[3] = 
                
pipe = ImPipeline(gray)

def grayscale(image):
    return color.rgb2gray(image)

def bwencode(image):
    # get blocks
    blocks = get_blocks(image)
    # perform DCT on all of the blocks

def view_quant_levels(k):
    binim(idct2(pipe.step_focus(1)),title="no quantization") # show without quantization
    for i in np.arange(1,k):
        quant = quantize(pipe.step_focus(1),k=1/(i*i))
        binim(idct2(quant),title=str(i))

view_quant_levels(5)







#blocks = [get_blocks(ycbcr[:,:,i], dtype='uint8') for i in range(3)]
# = [grid_im(blocks[i], recal=False, dtype='uint8', show=False) for i in range(3)] # needs to be reshaped in next line
#better_grid = np.rot90(malformed_grid,1,(0,2))
#better_grid = np.rot90(better_grid,3,(0,1))
#plot_ycbcr(better_grid)
#dctonblocks = dct_on_grid(blocks[0])
#height = dctonblocks.shape[0]*dctonblocks.shape[2]
#width = dctonblocks.shape[1]*dctonblocks.shape[3]
#grid_im(dctonblocks, cmap=plt.cm.gray, title="%dx%d block at (%d,%d)"%(height,width, x, y))

