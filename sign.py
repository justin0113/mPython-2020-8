# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 15:12:56 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z=mc.player.getPos()
mc.setSign(x,y,z,63,0,"1","2","","0")