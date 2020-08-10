# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 16:00:19 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z, = mc.player.getTilePos()

mc.setBlock(x+1,y,z,12)
mc.setBlock(x-1,y,z,12)
mc.setBlock(x,y,z+1,12)
mc.setBlock(x,y,z-1,12)
