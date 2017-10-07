'''
	created by: Ricardo dos S A Nunes
	date: 10/04/2017
	class: NLP
	Assignment: HW4

	Current State:
	10/03: Break down the algorithm to make the dictionary for the transition table
'''
# Create a dictionary that will take dictionaries
likelihood = {}
with open("WSJ_POS_CORPUS_FOR_STUDENTS 2/WSJ_02-21.pos") as f_in:
	for line in f_in.readlines():
		line = line.split('\t', 1)
		if len(line) == 2:
			key = line[1].strip()
			value = line[0].strip()
			if key in likelihood:
				if value in likelihood[key]:
					likelihood[key][value]+=1
	            	#likelihood[key].append(value)
				else:
					likelihood[key][value]=1
			else:
				likelihood[key] = {}
				likelihood[key][value] = 1


transition = {}
transition['beggining_sentence'] = {}
with open("WSJ_POS_CORPUS_FOR_STUDENTS 2/WSJ_02-21.pos") as f_in:
	curr_line = f_in.readlines()
	for next_line in f_in.readlines():
		hold_line = next_line
		next_line = next_line.split('\t', 1)
		curr_line = curr_line.split('\t', 1)
		if len(curr_line) == 2:
			key = curr_line[1].strip()
			if len(next_line) == 2:
				value = next_line[1].strip()
				if key in transition:
					if value in transition[key]:
						transition[key][value] += 1
					else:
						transition[key][value] = 1
				else:
					transition[key] = {}
					transition[key][value] = 1
		else:
			key = next_line[1].strip()
			if key in transition['beggining_sentence']:
				transition['beggining_sentence'][key]+=1
			else:
				transition['beggining_sentence'][key] = 1
		curr_line = hold_line

print(likelihood['DT']['a'])
print(transition['beggining_sentence'])
