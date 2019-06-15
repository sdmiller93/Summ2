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

# print the prompt and set the variable file_again to whatever is entered
print("Type the filename again:")
file_again = input(">")

# setting variable txt_again - calling the open function on the file_again variable which has whatever was input by the user
txt_again = open(file_again)

# calling the read function on the txt_again variable
print(txt_again.read())

# close the files where open was called up
close(txt)
close(txt_again)
