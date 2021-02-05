from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time 

x,y,z = mc.player.getPos()
mc.executeCommand("gamemode adventure @a")
mc.executeCommand("weather clear")
while True:
    if mc.setBlock(x,y-1,z,4):
        mc.executeCommand("kill @a")
    elif mc.setBlock(x,y-1,z,169):
        mc.executeCommand("setworldspawn")
    elif mc.setBlock(x,y-1,z,57):
        mc.postToChat('winner')
        time.sleep(3)
        mc.postToChat('既然跑完了')
        time.sleep(3)
        mc.postToChat('就賜予你死亡吧!')
        mc.executeCommand("summon lightning_bolt")
        mc.executeCommand("summon lightning_bolt")
        mc.executeCommand("summon lightning_bolt")
        mc.executeCommand("summon lightning_bolt")
        mc.executeCommand("summon lightning_bolt")
        mc.executeCommand("summon lightning_bolt")
            
            
    