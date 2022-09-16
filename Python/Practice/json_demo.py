import jsonpickle

class Cat:
	def __init__(self, name, breed):
		self.name = name
		self.breed = breed
	c = Cat('Charles', 'Toby')

	#j = json.dump(c.__dict__)

with open('cat.json', 'w') as file:
	frozen = jsonpickle.encode(c) #creates file and adds in 
	file.write(frozen)
