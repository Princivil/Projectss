#Custom For Loop

#for num in [1, 2, 3]
#for char in 'Hi There'

def my_for(iterable, fn):  #works to print each element 
	iterator = iter(iterable)
	while True:
		try:  #if no issues will print
			thing = next(iterator)
		except StopIteration: 
			#print('END OF ITERATOR') #approach error that wouldn't normally see in for loop
										#signifies that iteration is done for all items and no more left to iterate.
			break
		else:
			fn(thing)

def square(x):
	return x*x

my_for([1,2,3,4,5], square)