# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 09:18:40 2020

@author: USER
"""

import time
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
time. sleep(5)

x,y,z= mc.player.getTilePos()

mc.setBlocks(x+25,y-1,z+25,x-25,y-1,z-25,57)

