# load the argv module and exists module
from sys import argv
from os.path import exists

# 3 arguments need to be passed when executing
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
# one line: in_file = open(from_file)
# second line: indata = in_file.read()
# no need to close from_file since it will automatically be closed after the read.() function
indata = open(from_file, 'r').read()


print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# opening the to_file with the intent of writing to it
out_file = open(to_file, 'w')

# write the contents of indata to out_file
out_file.write(indata)

print("Alright, all done.")

out_file.close()
