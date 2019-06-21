# The Office

from sys import exit


def dwight():
	print("Welcome to The Office.")
	print("Your desk mate is Dwight Schrute.")
	print("He's challenging you to a duel.")
	print("Do you:")
	print("1. Turn it into a prank against him")
	print("2. Accept the duel. Your hands are your weapon.")
	print("3. Scold him.")
	print("4. Seduce him.")
	print("5. Ignore him.")
		
	choice = input("> ")

	if choice == "1":
		print("Hello Jim.")
		jim()
	elif choice == "2":
		print("Hello Andy.")
		andy()
	elif choice == "3":
		print("Hello Jan.")
		jan()
	elif choice == "4":
		print("Hello Angela.")
		angela()
	elif choice == "5":
		print("Hello Stanley.")
		stanley()
	else:
		downsized()

def jim():
	print("Uh oh. Lover's quarrel.")
	print("There's an argument between Pam & Karen.")
	print("Whose side are you on?")
	
	side = input("> ")
	
	if "pam" in side:
		pam()
	if "karen" in side:
		print("That's just wrong.")
		exit(0)
	else:
		kevin()

def pam():
	print("True love.")
	print("An amazing opportunity has come up but you are forced to leave the comfort of your home.")
	print("Do you:")
	print("1. Take the opportunity!")
	print("2. Think about it, but ultimately decide that you can't leave Scranton.")

	choice = input("> ")

	if choice == "1":
		print("Welcome to art school.")
		exit(0)
	if choice == "2":
		print("You marry Roy and eventually fall into a depression.")
		exit(0)
	else:
		kevin()

def andy():
	print("Good news!")
	print("America's Next Acapella Sensation is coming to a town near you!")
	print("Do you follow your dreams and audition?")
	print("Or do you let the opportunity pass. Maybe you're a better salesman than artist.")

	choice = input("> ")
	
	if "audition" in choice:
		print("Your wreck of an audition is now made into a web auto-tuned classic.")
		print("You can't just sit here and cry.")
		exit(0)
	else:
		print("You decide to ask out Angela.")
		angela()

def creed():
	print("Cool beans.")
	print("Hey man, I live by the quarry. We should get together and throw things down there.")
	
	choice = input("> ")

	if "yes" or "okay" in choice:
		print("You have a fun night full of psychadellics.")
		print("But the cops are on to you.")
		meredith()
	if "no" in choice:
		print("Good choice.")
		exit(0)
	else:
		kevin()

def stanley():
	print("You get a raise!")
	print("What do you do with your money?")
	print("1. Move to Florida.")
	print("2. Buy lots and lots of meatballs.")

	choice = input("> ")

	if choice == "1":
		print("Florida Stanley is who you want on your Florida team.")
		exit(0)
	if choice == "2":
		print("You've been meatballed!")
		exit(0)
	else:
		kevin()

def kevin():
	print("""
		Oh the spring time thinks that it\'s the best. 
		And the fall time think that it\'s the best. 
		But gather round, peeps, I tell ya the truth. 
		Nothin' beats the cookie season that\'s the truth!
	""")
	print("Oscar needs you to keep a secret.")
	print("But there's also a turtle that needs urgent attention.")
	print("Do you focus your attention on Oscar's secret or help the turtle?")

	choice = input("> ")
	
	if "oscar" or "Oscar" or "secret" in choice:
		print("Oh no, this just got more difficult.")
		print("The Senator is here!")
		senator()
	if "turtle" in choice:
		print("You are enormously proud of what you did for that turtle!")
		exit(0)
	else:
		print("I'm sorry, I don't understand.")
	
def angela():
	print("What color streamers?")
	print("Orange or green?")

	choice = input("> ")
		
	if choice  == "orange":
		print("I think orange is whore-ish.")
		exit(0)
	if choice == "green":
		print("God help you.")
		exit(0)
	else:
		kevin()

		
def downsized():
	print("You've been downsized.")
	exit(0)

def meredith():
	print("Meredith asks you inside for some vienna sausages.")
	exit(0)

def jan():
	print("Meeting with corporate!")
	print("David Wallace asks you for a private meeting.")
	print("Is this to discuss:")
	print("1. Your management technique.")
	print("2. An interview for someone's position.")
	print("3. An exciting investment opportunity.")

	choice = input("> ")

	if choice == "1":
		print("How about we order some pasta?")
		exit(0)
	if choice == "2":
		michael()
		exit(0)
	if choice == "3":
		print("You are now part owner of SUCK IT!")
		exit(0)
	else:
		print("Learn to type numbers.")

def michael():
	print("Conference room!")
	print("You're having a rough day. How do you lift your spirits?")
	print("1. Go to Benihana.")
	print("2. Go to Sandals Jamaica.")
	print("3. Make out with Holly.")

	choice = input("> ")

	if choice == "1":
		print("Dwight is showing you how to kill a chicken.")
		exit(0)
	if choice == "2":
		print("I've got!")
		print("Two tickets to PARADISE!")
		print("Pack your bags, we're leaving dayaftertomorrow!")
		exit(0)
	if choice =="3":
		print("Have you seen Pam?")
		print("Or Karen from behind?")
		exit(0)
	else:
		print("I'm sorry, I don't understand.")

def senator():
	print("You're torn between sexes.")
	print("Angela is the classic blond wife on your arm.")
	print("But Oscar is looking very fit. Lots of vigorous exercise.")
	print("Who do you choose?")

	choice = input("> ")

	if "Angela" or "angela" in choice:
		angela()
	if "Oscar" or "oscar" in choice:
		kevin()
	else:
		print("I'm sorry, I don't understand.")

def oscar():
	print("It's casual Friday.")
	print("You're wearing sandals but Angela has a problem with it.")
	print("Do you confront Angela or let it go?")

	choice = input("> ")

	if "confront" in choice:
		toby()
	if "let" in choice:
		print("Angela is bringing the confrontation to you!")
		toby()
	else:
		print("I'm sorry, I don't understand.")

def toby():
	print("Angela thinks that Oscar's feet are gross.")
	print("But everyone is complaining about Meredith's choice for casual Friday.")
	print("You go to talk to Meredith and give her some suggestions.")
	print("Do you ask her to 1) pull it down a touch?")
	print("Or do you 2) ask her to change completely?")
	
	choice = input("> ")

	if choice == "1":
		print("Meredith: You're all a bunch of prudes.")
		print("Kelly: Too far! Too far, Meredith!")
		print("Oscar: Meredith, your boob is out.")
		print("This is your fault.")
		downsized()

	if choice == "2":
		print("You're cancelling casual Friday.")
		exit(0)

	else:
		print("Learn to type numbers, man.")


dwight()
