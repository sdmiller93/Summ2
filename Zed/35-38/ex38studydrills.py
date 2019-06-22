# Doing Things to Lists
# when you write mystuff.append('hello')
	# 1. python sees you mentioned mystuff and looks up that variable
	# 2. it reads the . operator and starts to look at variables that are a part of mystuff
	# 3. it then hits append and compares the name to all the names that mystuff says it owns. 
		# if append is in there (it is), then python grabs that to use. 
	# 4. python sees the ( and says "Oh hey, this should be be a function."
		# it calls the function like normal but it calls the function with an extra argument
	# 5. the extra argument is.. mystuff
		# what happens at the end of all of this, is a function call that looks like append(mystuff, 'hello')

######################################################################################################################

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

# split(ten_things) and store in variable 'stuff'
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", 
	"Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	# pop(more_stuff) 
	next_one = more_stuff.pop()
	print("Adding: ", next_one)
	# append(stuff)
	stuff.append(next_one)
	print(f"There are {len(stuff)} items now.")
	
print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # what? cool!
print('#'.join(stuff[3:5])) # super stellar!

