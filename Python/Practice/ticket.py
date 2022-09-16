from random import randint
#Children under 5 are free
#Kids and Seniors are $5
#Adults are $10
age = randint(1,100)

if not((age>=2 and age <=8) or age >=65):
	print(f"Age {age}: You pay $10 since you're an adult.")
elif ((age>=2 and age <=8) or age >=65):
	print(f'Age {age}: That\'ll be $5')
else:
	print(f"Age {age}: You're free welcome!")