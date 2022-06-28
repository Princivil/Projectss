for x in range(1,21):
	if x % 2 == 0 and x != 4:
		print(f'{x} is even')
	elif x % 2 == 1 and x != 13:
		print(f'{x} is odd')
	else:
		print(f'{x} is unlucky')