import sys

def printOdds(maxVal):
	for i in range( 1, maxVal, 2):
		print(i)

printOdds(int(sys.argv[1]))
