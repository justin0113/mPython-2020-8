# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 12:19:16 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z=mc.player.getTilePos()

def plantTree(x,y,z):
    mc.setBlocks(x+1,y+5,z+1,x-1,y+3,z-1,17)
    mc.setBlocks(x,y,z,x,y+4,z,18)
for j in range(0,100,10):
    for i in range(0,100,10):
        plantTree(x+i,y,z+j)