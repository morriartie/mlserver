from urllib2 import urlopen

def fhtml(string):
	utext = string
	utext = list(utext)
	thisonly = False
	taglevel = 0
	i = len(utext)-1
	while(i>=0):
		if(utext[i]=='<'):
			taglevel -= 1
			thisonly = True	
		if(utext[i]=='>'):
			taglevel+=1
		if(insideChk(taglevel)):
			del utext[i]
		elif(thisonly):
			del utext[i]
			thisonly = False
		i-=1
	return ''.join(utext).split('\n')

def insideChk(level):
	if(level>0):
		return True
	else:
		return False
		
def input_html(html):
	ur = urlopen(html).read()
	ur = ur.split('\n')
	new_list = ["",""]
	for line in range(len(ur)):
		new_list.append(fhtml(ur[line]))
	return new_list		
