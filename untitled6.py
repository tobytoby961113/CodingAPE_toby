from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getPos()
import random
color = random.randrange(0,16)

mc.setBlock(x,y,z,35,color)

for i in range(50):
    for j in range(50):
        color = random.randrange(0,16)
        mc.setBlock(x,y,z,35,color)
        x+=1
    x,y,z = mc.player.getPos()
    z=z+i
ID=mc.getPlayerEntityId('Kyleduolc1103')
A= random.randrange(0,16)
while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        block = mc.getBlockWithData(hit.pos)
        data = block.data
        if data > A:
            mc.postToChat('NO')
        elif data < A:
            mc.postToChat('NO')
        else:
            mc.setBlock(hit.pos,46)
            mc.postToTitle(ID,'Yaaaaaa')
            break
        
        