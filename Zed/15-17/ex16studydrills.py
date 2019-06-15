# import the argv module 
from sys import argv

# the two arguments to be passed when executing this script
script, filename = argv

# will erase the passed file and give prompt to either continue or stop
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# will give a ? when asking for user input
input("?")

# assign variable target by opening the passed file, with the purpose of writing to it hence the 'w'
print("Opening the file...")
target = open(filename, 'w')

# variable.function in this case, truncate
print("Truncating the file. Goodbye!")
target.truncate()

# asking for 3 seperate lines of input
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to my file.")

# target (the file that was opened and read in) module write to it the three lines invoking new lines after each input wih the \n
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# close (save) the file
print("And finally, we close it.")
target.close()
