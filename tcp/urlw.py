from urllib2 import urlopen

def fhtml(string):
	#utext = urlopen(string).read()
	utext = string
	utext = list(utext)
	inside = False
	thisonly = False
	i = len(utext)-1
	while(i>0):
		if(utext[i]=='<'):
			inside = False
			thisonly = True
		if(utext[i]=='>'):
			inside = True
		if(inside):
			del utext[i]
		elif(thisonly):
			del utext[i]
			thisonly = False
		i-=1
	return ''.join(utext).split('\n')

def input_html(html):
	ur = urlopen(html).read()
	ur = ur.split('\n')
	new_list = ["",""]
	for line in range(len(ur)):
		new_list.append(fhtml(ur[line]))
	return new_list		


