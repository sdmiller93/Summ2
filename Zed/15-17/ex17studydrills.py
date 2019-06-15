# load the argv module and exists module
from sys import argv
from os.path import exists

# 3 arguments need to be passed when executing
script, from_file, to_file = argv

# no need to close from_file since it will automatically be closed after the read.() function

# how to open, read, and write to copy in_file to out_file in one line

 = open(from_file, r+w).write
