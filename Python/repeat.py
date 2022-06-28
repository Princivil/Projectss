times = input('How many times do I have to tell you? ')

for time in range(int(times)):
	print('Wash the dishes!')
	if time >= 2:
		print('You don\'t even listen. \n I\'m sending you to Grandma\'s')
		break