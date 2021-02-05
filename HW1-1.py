from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getPos()

mc.setBlock(x+1,y-1,z+1,57)
mc.setBlock(x+1,y-1,z-1,57)
mc.setBlock(x-1,y-1,z+1,57)
mc.setBlock(x-1,y-1,z-1,57)

mc.setBlock(x+2,y-1,z,1)
mc.setBlock(x-2,y-1,z,1)
mc.setBlock(x,y-1,z+2,1)
mc.setBlock(x,y-1,z-2,1)

mc.setBlock(x,y-1,z,11)
