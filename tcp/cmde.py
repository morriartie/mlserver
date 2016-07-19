def loadCommandsFromFile(filename):
	txt = open(filename).read().split('\n')
	for i in range(len(txt)):
		txt[i] = txt[i].split()
	return txt
	
