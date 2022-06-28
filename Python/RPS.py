from random import randint

print('Rock....')
print('Paper...')
print('Scissors...')


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




player = input("Player, make your move: ").lower()
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
	else:
		print("computer wins!")
elif player == "paper":
	if computer == "rock":
		print("player wins!")
	else:
		print("computer wins!")
elif player == "scissors":
	if computer == "paper":
		print("player wins!")
	else:
		print("computer wins!")	
else:
	print("Please enter a valid move!")