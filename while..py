# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:37:43 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time 
while True:
    x,y,z=mc.player.getTilePos()
    
    
    mc.postToChat("我正在看你X:"+str(x)+"Y:"+str(y)+"Z:"+str(z))
    time.sleep(0.5)
    
    
    
    
    
    
    
    