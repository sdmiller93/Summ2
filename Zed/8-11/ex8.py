# tells how to format the variables entered in each format(variable)
formatter = "{} {} {} {}"

# formatter tells how to format the entires, .format = telling it to invoke formatting, ( entries/variables)
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter)

# open parantheses (yay my first one!) 
print(formatter.format(
	"Roses are red",
	"Violets are blue.",
	"I could go for a shot of Whiskey", 
	"Or two."
))
