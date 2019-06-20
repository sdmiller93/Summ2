print("""You enter a dark room with two doors.
Do you go though door #1, #2, #3, or #4?""")

door = input("> ")

if door == "1":
	print("There's a giant bear here eating a cheese cake.")
	print("What do you do?")
	print("1. Take the cake.")
	print("2. Scream at the bear.")

	bear = input("> ")
	
	if bear == "1":
		print("The bear eats your face off. Good job!")
	elif bear == "2":
		print("The bear eats your legs off. Good job!")
	else:
		print(f"Well, doing {bear} is probably better.")
		print("Bear runs away")


elif door == "2":
	print("You stare into the endless abyss at Cthulhu's retina.")
	print("1. Blueberries")
	print("2. Yellow Jacket Clothespins.")
	print("3. Understanding revolvers yelling melodies.")

	insanity = input("> ")
	
	if insanity == "1" or insanity == "2":
		print("Your body survives powered by a mind of jello.")
		print("Good job!")
	else:
		print("The insanity rots your eyes into a pool of muck.")
		print("Good job!")
	
elif door == "3":
	print("Baxter is here. And he's farting incessantly.")
	print("What do you do?")
	print("1. Grab some air freshener.")
	print("2. Throw a pillow at him.")
	print("3. Cover your nose and wait for it to dissipate.")

	baxter = input("> ")

	if baxter == "1":
		print("Too much pressure! The can explodes and now you both have butt infections.")
	elif baxter == "2":
		print("You're rude and die a terrible death.")

	elif baxter == "3":
		print("You're a gentleman and a scholar.")

elif door == "4":
	print("You're in the upside down")
	print("But it's a different kind of upside down.")
	print("This one is full of used car salesmen.")
	print("They are trying to talk you into buying a '95 altima with 0% down.")
	print("Do you:")
	print("1. Take the offer. Hey, a car is a car.")
	print("2. Tell that guy he sucks, punch him in the face, and walk away as the dealership explodes behind you.")

	upsidedown = input ("> ")

	if upsidedown == "1":
		print("You fool. Your car breaks down as you drive off the lot and your credit tanks.")
		print("Good job. Loser.")

	else: 
		print("You're Liam Neeson. Congratulations on being awesome.")

else:
	print("You stumble around in the dark and fall onto a knife.")
	print("Good job.")

