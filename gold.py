# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 16:16:33 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

while True :
    hits= mc.events.pollBlockHits()
    if len(hits)>0:
        hit= hits[0]
        x,y,z= hit.pos.x, hit.pos.y, hit.pos.z
        block= mc.setBlock(x,y,z,57)