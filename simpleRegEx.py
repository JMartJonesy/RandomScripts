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
			if beginChar.isdigit():
				if (not sVal.isdigit()) or (int(sVal) < int(beginChar) or int(sVal) > int(endChar)):
					return False
			else:
				if (sVal.isdigit()) or (ord(sVal) < ord(beginChar) or ord(sVal) > ord(endChar)):
					return False
			sIndex += 1
			pIndex += 5
		else:
			if (pIndex + 1) < len(pattern) and pattern[pIndex + 1] == '*':
				multiChar = patternVal
				while string[sIndex] == multiChar:
					sIndex += 1
				pIndex += 2
			else:
				print(sVal, " ", patternVal)
				if sVal != patternVal:
					return False
				sIndex += 1
				pIndex += 1
	print(sIndex, " ", len(string), " ", pIndex, " ", len(pattern))
	return (sIndex ==  len(string) and pIndex == len(pattern))

print(regex("aaii1", "a*[a-z].[1-9]"))
