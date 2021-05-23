# This was created using an evolutionary process.
# It's fron the seventh generation. It does well
# against other generated strategies but fairly
# poor against human created ones.

# samfromcadott 2021

import random

DEFECT = 0
COOPERATE = 1

def historyPercent(history, action, length):
	if history.shape[1] == 0:
		return 0.0

	N = length if length <= history.shape[1] else history.shape[1]
	percent = history[1, -N].sum() / N

	if action == DEFECT:
		return 1-percent
	else:
		return percent

def strategy(history, memory):
	choice = COOPERATE
	wronged = memory

	if (random.random() > 1.0) or (historyPercent(history, DEFECT, 5) > 0.625) or (memory is not None and memory == True):
		mem = True
	else:
		wronged = False

	if (True and memory) or (random.random() > 0.125) or (historyPercent(history, DEFECT, 16) > 0.25):
		choice = DEFECT

	return choice, wronged
