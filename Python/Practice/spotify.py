playlist = dict(
	Title = "Feels", 
	Author = 'Ayanna Princivil', 
	songs = [
		dict(Title = '3way', Artist = 'Teyanna Taylor', Duration = 3.5), 
		dict(Title = 'Feel', Artist = 'Post Malone feat. Kehlani', Duration = 2.47),
		dict(Title = 'Even', Artist = 'Chris Brown', Duration = 4)
		]
	)

total = 0
for song in playlist['songs']:
	total += song['Duration']

print(f'{total} minutes of listening.' )