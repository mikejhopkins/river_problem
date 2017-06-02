#!/bin/python
'''
Mike J. Hopkins
June 2, 2017
'''

# set up the inclusionary sets for each participant
rabbit   = [0,1]						# assuming we *might differentiate "to" and "towards"
elephant = [0]							# I guess no elephants are included?
monkey   = [2,3,4,5,6,7,8,9,10,11,12]	# actually, this set is [2,3,4...] (infinite)
parrot   = [1,2,3,4,5,6,7,8,9,10,11,12]	# how many monkeys can hold a parrot?


# iterate over all possibilities
possibilities = []
for r in rabbit:
	for m in monkey:
		for p in parrot:
			if p > m: continue # parrots cannot exceed monkeys
			animals = r + m + p
			print 'r('+`r`+') + m('+`m`+') + p('+`p`+') = '+`animals`
			if not animals in possibilities:
				possibilities.append(animals)

# print the final results
possibilities.sort()
print 'Possibilities:'+`possibilities`
	
