def multiTable(maxVal):
	padding = len(str(maxVal*maxVal))
	for i in range ( 1, maxVal + 1):
		for j in range( 1, maxVal + 1):
			val = str(i*j)
			print(val.rjust(padding), end=" ")
		print()

multiTable(12)
