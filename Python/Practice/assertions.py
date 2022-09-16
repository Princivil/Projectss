#def add_pos_nums(x,y):
#	assert x>0 and y>0, "Both numbers must be positive!"
#	return x+y



def eat_junk(food):
	assert food in ['pizza','candy', 'ice cream', 'fried butter'], 'Food must be a junk food!'
	return f'NOM NOM NOM I\'m eating {food} '

	food = input('Enter your food: ')

	print(eat_junk(food))