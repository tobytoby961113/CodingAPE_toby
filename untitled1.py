from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getPos()
def tree(x,y,z):
    mc.setBlocks(x+1,y+2,z,x+3,y+5,z+2,46)
    mc.setBlocks(x+2,y,z+1,x+2,y+4,z+1,152)
for i in range(10):
    for k in range(2):
        for j in range(2):
            tree(x,y,z)
            x=x+5

    


