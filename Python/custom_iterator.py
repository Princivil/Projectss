class Counter:
	def __init__(self, low, high):
		self.low = low
		self.high = high

		def __iter__(self):
			return iter()

		def __next__(self):  #need to define next() because self isn't iterable yet
			if self.current < self.high:
				num = self.current
				self.current += 1
				return num
			raise StopIteration




for n in Counter(50,55):
	print(n)