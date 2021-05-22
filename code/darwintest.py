from darwinStrategy import *
from createGeneration import *

a = Strategy(0xa032cb8)

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
# print(a.sourceCode())

b = 0x1FFFFFF
c = 0x2AAAAAA

print( hex(reproduce(b, c)) )

for i in range(10):
	print( hex(mutate(b)) )
