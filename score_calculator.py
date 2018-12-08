
#####################################################################################################################################################################################
#############																																							#############
#############												My solution																									#############
#############										Environment: Python 2.7.15 																							#############
#############																																							#############
#####################################################################################################################################################################################

def computer_frame_score(score_value):
	if len(score_value) == 1:
		return (int(score_value) if score_value.isdigit() else 10 if score_value == "X" else 0 )
	elif len(score_value) == 2:
		return (computer_frame_score(score_value[0]) + computer_frame_score(score_value[0]))
	else:
		return 0
	
def computer_score(line):
	frames = []
	frame_count = 0
	score = 0
	for i in range(0,12):
		if frame_count == 10:
			break
		if line[0] == 'X':
			score += computer_frame_score(line[0]) + computer_frame_score(line[1]) + (10 - computer_frame_score(line[1]) if "/" in line[1:3] else computer_frame_score(line[2]))
			line = line[1:]
		elif ((line[0].isdigit()) and (1<= int(line[0]) <=9 ))or ( (not line[0].isdigit()) and (line[0] == '-')) :
			score += computer_frame_score(line[0]) + ((computer_frame_score(line[2]) + 10 - computer_frame_score(line[0])) if "/" == line[1]  else computer_frame_score(line[1]))			
			line = line[2:] if len(line)>2 else ''
		frame_count += 1
	return score
	
if __name__ == '__main__':
	lines = ['XXXXXXXXXXXX','9-9-9-9-9-9-9-9-9-9-','5/5/5/5/5/5/5/5/5/5/5','X7/9-X-88/-6XXX81']
	for i in lines:
		print i, "\tscore :",computer_score(i)