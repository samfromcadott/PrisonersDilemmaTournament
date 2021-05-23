from darwinStrategy import *
from generation import *

a = Strategy(0xe5d4bae)

# print("Set memory: ", a.setMemory)
# print("Memory action: ", a.memoryAction)
# print("Check Memory: ", a.checkMemory)
# print("Action: ", a.action)
# print("Memory chance: ", a.memoryChance)
# print("Memory percent: ", a.memoryPercent)
# print("Memory length: ", a.memoryLength)
# print("Action chance: ", a.actionChance)
# print("Action percent: ", a.actionPercent)
# print("Action length: ", a.actionLength)
#
print(a.sourceCode())

# b = 0x1FFFFFF
# c = 0x2AAAAAA
#
# print( hex(reproduce(b, c)) )
#
# for i in range(10):
# 	print( hex(mutate(b)) )

gen = newGeneration([0x1FFFFFF,0x2AAAAAA,0x3CCCCCC,0x0BBBBBB])

for i in gen:
	print( hex(i) )
