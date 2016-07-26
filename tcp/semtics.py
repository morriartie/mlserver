import matplotlib.pyplot as plt
from random import randint

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
	# x values = known commands
	# y values = precision 
	# f(x) values = precision on each command
	# make a line where x range from 0 to number_of_commands and y equals to winner
	global plotFStoggled
	randColor = buildRandomColor()

	x = []
	y = []

	for i in range(len(checklist_list)):
		x.append(str(i))

	for j in range(len(res_collection)):
		y.append(str(res_collection[j]))

	plt.scatter(x,y,label=" ".join(inputed),color=randColor)
	plt.axis([0,len(x),0,110])
	plt.xlabel('Known commands')
	plt.ylabel('Precision')
	plt.title('Command history by precision')
	plt.legend(loc='center left', bbox_to_anchor=(1,0.5))
	if not(plotFStoggled):
		mng = plt.get_current_fig_manager()
		mng.full_screen_toggle()
		plotFStoggled = True
	plt.draw()
	plt.pause(0.0001)

def buildRandomColor():
	r,g,b = 10,10,10
	avr = 0
	while(avr<127):
		r = randint(0,255) 
		g = randint(0,255)
		b = randint(0,255)
		avr = (r+g+b)/3

	result = '#%02x%02x%02x' % (r,g,b)
	return result
	