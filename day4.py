from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random


x,y,z=mc.player.getTilePos()

for i in range(20):
    r=random.randrange(1,5)
    
    if r==1:
        mc.setBlocks(x,y,z,x+4,y,z,1)
        x=x+4
    if r==2:
        mc.setBlocks(x,y,z,x-4,y,z,1)
        x=x-4    
    if r==3:
        mc.setBlocks(x,y,z,x,y,z+4,1)
        z=z+4
    if r==4:
        mc.setBlocks(x,y,z,x,y,z-4,1)
        z=z-4
        
        
        
        
        
        
        
for i in range(10):
    x,y,z=mc.player.getTilePos()
    x=x+i
    
    for j in range(10):
        r=random.randrange(0,16)
        z=z+1
        mc.setBlock(x,y,z,35,r)
        
        
        
        
        
        
        
        
        
        
        
r=random.randrange(0,16)
while True:
    hits=mc.events.pollBlockHits()
    
    if len(hits)>0:
        hit=hits[0]
        
        block=mc.getBlockWithData(hit.pos)
        data=block.data

        if data==r:
            mc.postToChat('恭喜')
            mc.setBlock(hit.pos,57)
            break
        elif data<r:
            mc.postToChat('更大的ID')
            
        elif data>r:
            mc.postToChat('更小的ID')
            
            
            
myID=mc.getPlayerEntityId('XDDnightingale')
mc.postToTitle(myID,'efoefnwoba;fe')
        
        
list2d=[[46,0,46,46,46,46,46],
        [46,0,0,0,0,0,0,46],
        [46,0,46,46,46,0,46],
        [46,0,0,0,0,46,46]   ,     
        [46,0,46,46,46,0,46],
        [46,0,0,0,46,0,46],
        [46,46,46,46,46,0,46]]
        
x,y,z=mc.player.getTilePos()
startX=x
startZ=z

for j in range(4):
    for listld in list2d:
        
        for i in listld:
            mc.setBlock(x,y,z,i)
            x=x+1
        
        x=startX
        z=z+1
        
    z=startZ
    y=y+1


































        
        
        
        
        
        
        
        
        
        
        
        
        
        