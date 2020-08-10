# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 14:38:12 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x=273

y=144

z=25

mc.player.setTilePos(x,y,z)