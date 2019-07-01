# import mystuff # mystuff module

# mystuff.apple() # apple function
# print(mystuff.tangerine) # print the tangerine variable as defined in the mystuff module

#############################################################################################################

class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)

happy_bday = Song(["They rally around tha family", 
			"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

