# load the argv module 
from sys import argv

# the two arguments that need passed when executing the script.
script, input_file = argv

# create function called print_all with argument f, then print the contents of f with read.
def print_all(f):
	print(f.read())

# create a function called rewind with argument f, then 'rewind' by starting back at line 0 of the text file
def rewind(f):
	f.seek(0)

# create a function called print_a_line with the arguments line_count and f and then print the line_count variable and read f
def print_a_line(line_count, f):
	print(line_count, f.readline())

# opening the input_file (test.txt) and assign it to the variable current_file
current_file = open(input_file)


print("First let's print the whole file:\n")

# put current_file to new variable print_all 
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# call the rewind function on current_file
rewind(current_file)

print("Let's print three lines:")

# assigning current_line, 1. then use function print_a_line on current_line and current_file
current_line = 1
print_a_line(current_line, current_file)

# adding to current_line currently holding 1 so it will be 2 and then printing the line number and the string of text in the file
current_line = current_line + 1
print_a_line(current_line, current_file)

# current line number is 2, adding 1 so it is now 3. Printing that and the string of text on that line in the file. 
current_line = current_line + 1
print_a_line(current_line, current_file)

# so when creating a function you define it and give it a name, then in () give the arguments needed. 
# When you call on that function you must pass it that many arguments, the first being assigned to the first argument, second to the second, etc. 
# Then that function carries out the task that is written on the line below it. 
# for example; the rewind function has "f.seek(0)" so the second argument (the file) will return to line 0 by using seek and 0. 
