from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getPos()
a=input('你是誰?')
print('HI'+a+'我家門前有****,後面有*****')
mc.setBlocks(x+10,y+10,z+10,x-10,y-10,z-10,17)
mc.setBlocks(x+9,y+9,z+9,x-9,y-9,z-9,0)
y=y+9
mc.setBlocks(x+10,y,z+10,x-10,y,z-10,17)
mc.setBlocks(x+9,y-1,z+9,x-9,y-1,z-9,0)
