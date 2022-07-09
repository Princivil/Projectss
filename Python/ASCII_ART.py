import pyfiglet
from termcolor import colored

msg = input('What would you like to print? ')
color = input('What color?')
if color not in ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'): #best as tuple since this willl never change
	color = 'cyan'
	
art = pyfiglet.figlet_format(msg)
colored_art = colored(art, color = color)

print(colored_art)