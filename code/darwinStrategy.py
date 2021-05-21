from random import random

class Strategy(object):
	DEFECT = 0
	COOPERATE = 1

	def __init__(self, dna):
		self._dna = dna

		self.setMemory = bool(dna >> 27)
		self.memoryAction = (dna & (1<<26)) >> 26
		self.memoryChance = ( (dna & 0xF00000) >> 20) + 1
		self.memoryPercent = ( (dna & 0x0F0000) >> 16 )+ 1
		self.memoryLength = ( (dna & 0x00F000) >> 12 ) + 1

		self.checkMemory = bool((dna & (1<<25)) >> 25)
		self.action = (dna & (1<<24)) >> 24
		self.actionChance = ( (dna & 0x000F00) >> 8 ) + 1
		self.actionPercent = ( (dna & 0x0000F0) >> 4 ) + 1
		self.actionLength = (dna & 0x00000F) + 1


	def historyPercent(self, history, action, length):
		N = length if length <= history.shape[1] else history.shape[1]
		percent = N/sum( history[1, -N] )

		if action == DEFECT:
			return 1-percent
		else:
			return percent


	def strategy(self, history, memory):
		choice = self.action ^ 1
		mem = None

		if (random() < 1/self.memoryChance) or (self.historyPercent(history, self.memoryAction, self.memoryLength) > 1/self.memoryPercent):
			mem = self.setMemory

		if (self.checkMemory and memory) or (random() < 1/self.actionChance) or (self.historyPercent(history, self.action, self.actionLength) > 1/self.actionPercent):
			choice = self.action

		return choice, mem
