# strings are pieces of text you want to export out of the program 

# assign variables
types_of_people = 10
x = f"There are {types_of_people} types of people."

# assign more variables
binary = "binary"
do_not = "don't"

# write string with embedded variables
y = f"Those who know {binary} and those who {do_not}"

# printing strings/variables
print(x)
print(y)

# produce f string
print(f"I said: {x}")
print(f"I also said: '{y}'")

# set marker to false
hilarious = False

# {} at end of string allows for embedding of second variable in print further down
joke_evaluation = "Isn't that joke so funny?! {}"

# print statements
print(joke_evaluation.format(hilarious))

# set variables
w = "This is the left side of..."
e = "a string with a right side."

# print showing how to piece together two variables in one single string
# variable + variable = longer single variable because you are adding two pieces of text together on a single line the computer views it as just x and y (or w and e here)
print(w + e)

