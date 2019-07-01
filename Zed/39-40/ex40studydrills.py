# write some more songs using this and make sure you understand that you're passing a list of strings as the lyrics
# helpful link: https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/

# create a class called Song -- class <ClassName>(superclass) in the absence of anything else, the superclass should always be object, the root of all classes in Python
class Song:
	
	# create the constructor to be called when an object is created - allows the class to initialize the attributes of a class
	def __init__(self, lyrics):
		self.lyrics = lyrics # the self keyword can access the attributes and methods of the class created
	def sing(self):
		for line in self.lyrics:
			print(line)  # create a function called sing and when called will print the string associated with the first appendage

tears_for_fears = Song(["Everybody wants to rule the world."])

harry_james = Song(["Kiss me once",
			"Then kiss me twice",
			"And kiss me once again.", 
			"It's been a long, long, time."])

tears_for_fears.sing()

harry_james.sing() 

# put the lyrics in a separate variable, then pass that variable to the class to use instead. 


