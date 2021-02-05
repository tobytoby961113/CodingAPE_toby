from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getPos()
number = 1
import time
time.sleep(5)
for i in range(5):
    for i in range(number):
        mc.spawnEntity(x,y,z,20)
        number*2