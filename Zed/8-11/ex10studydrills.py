# the \t indents the line or "tabs" in
tabby_cat = "\tI'm tabbed in."

# the \n puts it on a new line
persian_cat = "I'm split\non a line."

# \\ a \\ types it like this --> \ a \ 
backslash_cat = "I'm \\ a \\ cat."

# the single ''' is easier to read so you can ensure you have 3 versus this """ which is a bit harder to see at a glance. 
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# number 3: combine escape sequences and format strings to create a more complex format
# assign variables
spongebob = "spongebob squarepants"
squidward = "squidward tentacles"
work = "Krusty Krab"
play = f"\t{spongebob} likes to play at Jellyfish fields"
employment = f"They both work at the \n{work}"

print(f"Under the sea lives {spongebob} and {squidward}.")
print(play)
print(employment)

friends = "{} {} {}" 
print(friends.format("Sandy", "Patrick", "Larry"))

menu = '''
Menu:
\t-Krabby Patty
\t-Soda
\t-Fries
'''

print(menu)

