def colorize(text, color):
	colors = ('cyan', 'yellow', 'magenta')
	if type(text) is not str:
		raise TypeError('text must be instance of str')
	if color not in colors:
		raise ValueError('color is invalid color')
	print(f'Printed {text} in {color}')

colorize('hello', 'red')

#Raises error if incorrect color input