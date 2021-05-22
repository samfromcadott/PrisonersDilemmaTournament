from random import randint

def firstGeneration(n):
	# The first generation should be totally random
	gen = []

	for i in range(n):
		gen.append( randint(0, 0xFFFFFFF) )

	return gen


def mask():
	return 0xF * randint(0,1) | (0xF<<4) * randint(0,1) | (0xF<<8) * randint(0,1) | (0xF<<12) * randint(0,1) | (0xF<<16) * randint(0,1) | (0xF<<20) * randint(0,1) | (1<<24) * randint(0,1) | (1<<25) * randint(0,1) | (1<<26) * randint(0,1) | (1<<27) * randint(0,1)


def reproduce(a, b):
	m = mask()

	sperm = a & m
	egg = b & (m ^ 0xFFFFFFF)

	return sperm | egg


def mutate(strat):
	if randint(0, 4) == 0: # 1 in 5 chance of mutation
		N = randint(1, 10) # Number of bits to flip

		for i in range(N):
			strat = strat ^ (1<<randint(0, 27))

	return strat


def writeGeneration(gen, number):
	f = open('gen%04i.txt' % number, 'w+')

	for i in gen:
		f.write( hex(i) + '\n')

	f.flush()
	f.close()
