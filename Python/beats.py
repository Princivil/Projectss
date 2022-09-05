def current_beat()
	i = 0
	nums = (1,2,3,4)
	while True:
		if i >= len(nums): i = 0
		yield nums[i]
		i +=1
#creates infinite beats loop

