age = input('How old are you?\n')
if age:
	age = int(age)
	if age >= 18 and age <21:
		print("you can enter but don't go by the bar!")
	elif age >= 21:
		print('Go ahead buddy!')
	else:
		print('Scram no kids allowed!!')
else:
	print('TELL ME YOUR AGE!!')