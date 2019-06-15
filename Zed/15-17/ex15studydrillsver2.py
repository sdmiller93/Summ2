# load the argv module
from sys import argv

# this requires two arguments to be passed when the script is executed. In this case, python3 scriptname textfile
script, filename = argv

# txt is the variable
# open is the module and you are opening a specific file
txt = open(filename)

# print string with entered txt file filename.
print(f"Here's your file {filename}:")

# calling the read function on the variable we set earlier, txt which holds our text file
print(txt.read())
 
# by ending the script here, it doesn't prompt any user input and instead just prints the contets of the passed text file


