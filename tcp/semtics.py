import matplotlib.pyplot as plt
from random import randint
from math import sqrt

accept_precision_above = 40
plotFStoggled = False

def compareSample(sample, checklist):
	matches = 0
	sample = filterWords(sample)
	for x in range(len(sample)):
		for y in range(len(checklist)):
			if(sample[x]==checklist[y]):
				matches+=1
	matches = float(matches)
	checklistN = float(len(checklist))
	div = matches/checklistN
	fr = div*100
	return fr	

def filterWords(unfiltered):
	unfiltered = " ".join(unfiltered).lower().split()
	etc = "is a by of the in to from and".split()
	per_pronouns = "i me we us you she her he him it they them".split()
	rel_pronouns = "that which who whom whose whichever whoever whomever".split()
	dem_pronouns = "this that these those".split()
	ind_pronouns = "both few many several all any most none some".split()
	inddpronouns = "anybody anyone anything each either everybody everyone everything neither nobody no one nothing one somebody someone something".split()
	ref_pronouns = "myself ourselves yourself yourselves himself herself itself themselves".split()
	int_pronouns = "what who which whom whose".split()
	pos_pronouns = "my your his her its our their mine yours his hers ours theirs".split()
	wordlist = per_pronouns+rel_pronouns+dem_pronouns+ind_pronouns+inddpronouns+ref_pronouns+int_pronouns+pos_pronouns+etc
	for x in range(len(unfiltered)):
		for y in range(len(wordlist)):
			if(unfiltered[x]==wordlist[y]):
				unfiltered[x]=""
	filtered = " ".join(unfiltered)
	filtered = filtered.split() 
	return filtered

def findWinner(sample, checklist_list):
	prec_res = [0 for i in range(len(checklist_list))]
	winner = -1
	last_res = -1
	for x in range(len(checklist_list)):
		res = compareSample(sample, checklist_list[x])
		prec_res[x] = res
		if(res>last_res):
			last_res = res
			winner = x
	print("Winner: "+" ".join(checklist_list[x])+" with "+str(last_res)+"%")		
	buildPlot(sample, checklist_list, prec_res, winner)
	if(notCommandFilter(last_res)):
		winner = (-1)	
	return winner		

def notCommandFilter(precision):
	if(precision <= accept_precision_above):
		return True
	else:
		return False

def buildPlot(inputed, checklist_list, res_collection, winner):
	#initialization
	global plotFStoggled
	randColor = buildRandomColor()
	x = []
	y = []
	#fill the lists
	for i in range(len(checklist_list)):
		x.append(str(i))
	for j in range(len(res_collection)):
		y.append(str(res_collection[j]))
	#plot bg color
	plt.subplot(axisbg='#333333')	
	#build plot	
	plt.scatter(x,y,label=" ".join(inputed),color=randColor)
	plt.axis([0,len(x),-10,110])
	plt.xlabel('Known commands')
	plt.ylabel('Precision')
	plt.title('Command history by precision')
	plt.legend(loc='center left', bbox_to_anchor=(1,0.5))
	#toggle full screen only once
	if not(plotFStoggled):
		mng = plt.get_current_fig_manager()
		mng.full_screen_toggle()
		plotFStoggled = True
	#build lines connecting results
	plt.plot(x,y,color=randColor,linewidth=4.0)
	#show plot	
	plt.draw()
	plt.pause(0.0001)

def buildRandomColor():
	b_lowerLimit , b_upperLimit = 159 , 255 #std:159 ~ 255
	dog_lowerLimit , dog_upperLimit = 0.7 , 1 #std: 0.7 ~ 1
	r,g,b = randint(0,255),randint(0,255),randint(0,255)
	avr = (r+g+b)/3 #average (brightness)
	std_d = sqrt((((r-avr)**2)+((g-avr)**2)+((b-avr)**2))/3) #standard deviation
	degree_of_grey = std_d/121 # Values between 0 and 1, 0 is not gray and 1 is gray
	#accept only visible colors
	while((avr<b_lowerLimit or avr>b_upperLimit) and (degree_of_grey<dog_lowerLimit or degree_of_grey>b_upperLimit)):
		r = randint(0,255) 
		g = randint(0,255)
		b = randint(0,255)
		avr = (r+g+b)/3
		std_d = ((r-avr)**2)+((g-avr)**2)+((b-avr)**2)
		degree_of_grey = std_d/121
		print("("+str(r)+","+str(g)+","+str(b)+")|avr:"+str(avr)+"|std_d:"+str(std_d)+"|dog:"+str(degree_of_grey))
	#convert grb to hexadecimal	
	result = '#%02x%02x%02x' % (r,g,b)
	return result

	