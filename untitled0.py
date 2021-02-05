from mcpi.minecraft import Minecraft
mc = Minecraft.create()

for i in range(20):
    x,y,z = mc.player.getPos()
    x+=i
    mc.setBlock(x,y-1,z,57)
mc.setBlocks(x+5,y+5,z+5,x-5,y-5,z-5,57)
mc.setBlocks(x+4,y+4,z+4,x-4,y-4,z-4,46)
mc.setBlocks(x+6,y+6,z+6,x-5,y+6,z-5,70)