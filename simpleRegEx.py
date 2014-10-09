def regex( string, pattern ):

	sIndex = 0
	pIndex = 0
	
	while sIndex < len(string) and pIndex < len(pattern):
		patternVal = pattern[pIndex]
		sVal = string[sIndex]
		if patternVal == '.':
			sIndex += 1
			pIndex += 1
		elif patternVal == '[':
			beginChar = pattern[pIndex + 1]
			endChar = pattern[pIndex + 3]
			if ord(sVal) < ord(beginChar) or                                                   ord(sVal) > ord(endChar):
				return False
			sIndex += 1
			pIndex += 5
		else:
			if (pIndex + 1) < len(pattern) and                                                  pattern[pIndex + 1] == '*':
				multiChar = patternVal
				while string[sIndex] == multiChar:
					sIndex += 1
				pIndex += 2
			else:
				if sVal != patternVal and                                                          ((sIndex - 1) > 0 and                                                           (pIndex - 2) > 0) and                                                           patternVal[pIndex - 1] == '*' and                                              patternVal[pIndex - 2] != string[sIndex - 1]:
					return False
				if sVal == patternVal:
					sIndex += 1
				pIndex += 1
	return (sIndex ==  len(string) and pIndex == len(pattern))

print(regex("aaai1", "a*a.[1-9]"))
