from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getPos()

x1 = []
y1 = []
z1 = []

for i in range(1,4):
    x1.append(5*i)
for i in range(1,4):
    y1.append(6*i)
for i in range(1,4):
    z1.append(7*i)
    
mc.setSign(x,y,z,63,2,str(x1),str(y1),str(z1))
mc.setBlock(x,y-1,z,46)
mc.setBlock(x,y-2,z,152)