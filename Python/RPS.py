from random import randint



#-----------------------------------------

##Run into issue where something goes wrong no matter how I adjust the moves

#p1 = input('Player 1 make your move: ')
#p2 = print('PC make your move:' + random.choice(['rock','paper','scissors']))

#if p1 == p2:
#	print('Draw!\n Rematch...')
#elif p1 == 'rock' and p2 == 'scissors':
#	print('Player 1 wins!')
#elif p1 == 'paper' and p2 == 'rock':
#	print('Player 1 wins!')
#elif p1 == 'scissors' and p2 == 'paper':
#	print('Player 1 wins!')
#elif p2 == 'rock' and p1 == 'scissors':
#	print('PC wins!')
#elif p2 == 'paper' and p1 == 'rock':
#	print('PC wins!')
#elif p2 == 'scissors' and p1 == 'paper':
#	print('PC wins!')
#else:
#	print('Something went wrong :{')

#-----------------------------------------


win1 = 0
win2 = 0

while win1 < 3 and win2 < 3:  #3 is number of wins
	print(f'Player: {win1}  Computer: {win2}')
	print('Rock....')
	print('Paper...')
	print('Scissors...')

	player = input("Player, make your move: ").lower()
	if player == 'quit' or player == 'q':
		break	
	rand_num = randint(0,2)
	if rand_num == 0:
		computer = "rock"
	elif rand_num == 1:
		computer = "paper"
	else:
		computer = "scissors"

	print(f"Computer plays {computer}" )

	if player == computer:
		print("It's a tie!")
	elif player == "rock":
		if computer == "scissors":
			print("player wins!")
			win1 += 1
		else:
			print("computer wins!")
			win2 += 1
	elif player == "paper":
		if computer == "rock":
			print("player wins!")
			win1 += 1
		else:
			print("computer wins!")
			win2 += 1
	elif player == "scissors":
		if computer == "paper":
			print("player wins!")
			win1 += 1
		else:
			print("computer wins!")	
			win2 += 1
	else:
		print("Please enter a valid move!")
if win1 > win2:
	print('Congrats you win!')
elif win1 == win2:
	print('No one won!')
else:
	print('Sorry, the Computer won!')

#___________________
#IMPROVED




