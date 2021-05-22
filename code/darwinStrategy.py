import random

class Strategy(object):
	DEFECT = 0
	COOPERATE = 1

	# DNA bitfield structure
	# 1 bit		Set memory true/false
	# 1 bit		Check for purple defection/cooperation
	# 1 bit		Check memory
	# 1 bit		Action defect/cooperate
	# 4 bits	Random memory setting
	# 4 bits	Percent of last purple moves for action setting
	# 4 bits	Number of last purple moves for memory setting
	# 4 bits	Random action chance
	# 4 bits	Percent of last purple moves for action setting
	# 4 bits	Number of last purple moves for action setting

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
		if history.shape[1] == 0:
			return 0.0

		N = length if length <= history.shape[1] else history.shape[1]
		percent = history[1, -N].sum() / N

		if action == self.DEFECT:
			return 1-percent
		else:
			return percent


	def strategy(self, history, memory):
		choice = self.action ^ 1
		mem = memory

		if (random.random() > self.memoryChance * 0.0625) or (self.historyPercent(history, self.memoryAction, self.memoryLength) > self.memoryPercent * 0.0625) or (memory is not None and memory == self.setMemory):
			mem = self.setMemory
		else:
			mem = not self.setMemory

		if (self.checkMemory and memory) or (random.random() > self.actionChance * 0.0625) or (self.historyPercent(history, self.action, self.actionLength) > self.actionPercent * 0.0625):
			choice = self.action

		return choice, mem


	def sourceCode(self):
		return (
			"import random\n\n"

			"DEFECT = 0\n"
			"COOPERATE = 1\n\n"

			"def historyPercent(history, action, length):\n"
			"	if history.shape[1] == 0:\n"
			"		return 0.0\n\n"

			"	N = length if length <= history.shape[1] else history.shape[1]\n"
			"	percent = history[1, -N].sum() / N\n\n"

			"	if action == DEFECT:\n"
			"		return 1-percent\n"
			"	else:\n"
			"		return percent\n\n"


			"def strategy(history, memory):\n"
			f"	choice = {self.action ^ 1}\n"
			"	mem = memory\n\n"

			f"	if (random.random() > {self.memoryChance * 0.0625}) or (historyPercent(history, {self.memoryAction}, {self.memoryLength}) > {self.memoryPercent * 0.0625}) or (memory is not None and memory == {self.setMemory}):\n"
			f"		mem = {self.setMemory}\n"
			"	else:\n"
			f"		mem = {not self.setMemory}\n\n"

			f"	if ({self.checkMemory} and memory) or (random.random() > {self.actionChance * 0.0625}) or (historyPercent(history, {self.action}, {self.actionLength}) > {self.actionPercent * 0.0625}):\n"
			f"		choice = {self.action}\n\n"

			"	return choice, mem\n"
		)
