from random import randint

guess = int(input('Guess a number 1 - 10: '))
num = randint(1,10)

while True:
	if guess < num:
		print('Too low!')
		guess = int(input('Guess a number 1 - 10: '))
	elif guess > num:
		print('Too high!')
		guess = int(input('Guess a number 1 - 10: '))
	else:
		print(f'You win, {num} is correct!')
		again = input('Do you want to play again? (y/n) ')
		if again == 'y':
			num = randint(1,10)
			guess = int(input('Guess a number 1 - 10: '))
		else:
			print('Thank you for playing!')
			break


