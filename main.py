from time import sleep
import mcpi.minecraft as minecraft
import sys
import mcpi.block

mc = minecraft.Minecraft.create()

"""

mc.postToChat('Hello and welcome to Mast World')
mc.postToChat('Climb to the 20th floor!')

repeat = True
while int(mc.player.getPos().y) != int(20):
    #block = mc.getBlock(1, 1, 1)
    # print(block)
    # print(mc.getPlayerEntityIds())

    if int(mc.player.getPos().y) >= int(15) and int(mc.player.getPos().y) < int(20):
        if repeat == True:
                mc.postToChat("OMG, you are so close!")
                repeat = False
    sleep(1)
mc.postToChat('Good Job!')
"""
while True:
    playerPos = mc.player.getPos()
    playerPos = minecraft.Vec3(int(playerPos.x), int(playerPos.y), int(playerPos.z))
    mc.setBlock(playerPos.x,playerPos.y-1,playerPos.z,mcpi.block.DIAMOND_BLOCK)
