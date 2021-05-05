import random

def GeneticAlgorithm():
	
	# input values
	objs = ['item1', 'item2', 'item3', 'item4']
	w    = [11, 34, 75, 2] # weight
	v    = [7, 2, 1, 9] # value

	# weight combination lists
	s1 = [1, 1, 0, 0 ]
	s2 = [0, 1, 1, 0 ]
	s3 = [0, 0, 1, 1 ]
	s4 = [1, 0, 1, 0 ]
	s5 = [0, 1, 0, 1 ]
	s6 = [1, 1, 0, 1 ]
	s7 = [0, 1, 1, 1 ]
	s8 = [1, 1, 1, 0 ]
	
	sList = [s1, s2, s3, s4, s5, s6, s7, s8]
	sumW  = []
	knights = []


	print('\n---------------------------------------------')
	print('calcualte the total wieght of each combination')
	
	# loop each combination list
	for x in sList:
		i=0 # index
		sum = 0 # start
		print('\ns:{}'.format(x)) # current soluction set
		
		# loop items of the current combination list
		for y in x:
			if y == 1:
				sum = sum + w[i] # add value to sum
				print('   + {}'.format(w[i]))
			i=i+1
		print('   sum = {}'.format(sum))
		
		
		if sum > 100: # if weight is greater the sack limit
		    sum = 0
		sumW.append(sum) # add all total values to list
		
		if sum != 0:
		    knights.append(sum)
		
	print ('\nwieght of each soluction: {}'.format(sumW))


	print('\n---------------------------------------------')
	print('Selection: Tournament Selection')
	
	"""	
	d = {}
	for x in range(len(sumW)):
	    if sumW[x] != 0:
	        d['{}'.format(sList[x])] = sumW[x]
	print(d)
	"""
	print(knights)
	round2 = []
	round3 = []
	
	# Round 1
	print('\n--------- START ROUND ONE')
	while knights:
		
		# choose players
		rand = random.randint(0, len(knights)-1)
		p1 = knights.pop(rand)
		p2 = knights.pop(0)
		print('{} vs {}'.format(p1, p2))
		
		# FIGHT!!!
		if p1 >= p2:
			round2.append(p1)
			print('{} wins\n'.format(p1))
		else:
			round2.append(p2)
			print('{} wins\n'.format(p2))
		
		n = len(knights)
		if n == 1:
		    break
		print(knights)

	
	# Round 2
	print('\n--------- START FINALS')
	while round2:
		
		# choose players
		rand = random.randint(0, len(round2)-1)
		p1 = round2.pop(rand)
		p2 = round2.pop(0)
		print('{} vs {}'.format(p1, p2))
		
		# FIGHT!!!
		if p1 >= p2:
			round3.append(p1)
			print('{} wins\n'.format(p1))
		else:
			round3.append(p2)
			print('{} wins\n'.format(p2))
		
		n = len(round2)
		if n == 1:
		    break

		print('WINNER: {}'.format(round3))

GeneticAlgorithm()



