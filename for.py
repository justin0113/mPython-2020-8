# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 10:40:56 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z=mc.player.getTilePos()

for j in range(3):
    for i in range(20):
        mc.setBlock(x+i,y-1,z+i+j,171,13)