# import sys module 
import sys

# when executing, pass the script name, input encoding (ex: utf-8), and error (he used strict)
script, input_encoding, error = sys.argv

# create function called main with arguments; language file, encoding, errors)
# read one line from the language file it is given
def main(language_file, encoding, errors):
	line = language_file.readline()

# if statement: if line has something in it (readline function will return empty once it reaches the end of the file) 
# this tests for the empty string, as long as the line has something, it returns true and the code under it will run. If false, it will skip
# calling main inside main causes the script to loop until the line becomes empty (at the end of the file) at which point it will complete, and print.
	if line:
		print_line(line, encoding, errors)
		return main(language_file, encoding, errors)

# create function print_line with arguments; line, encoding, and errors
# line.strip() is removing the trailing \n on the line string. 
# encode it into raw bytes
# next_lang is a string so it needs encoded (decode bytes, encode strings) - passes the encoding he wants and how to handle errors
# cooked_string  contains the raw bytes and therefore needs decoded. This string should be the same as the next_lang string
def print_line(line, encoding, errors):
	next_lang = line.strip()
	raw_bytes = next_lang.encode(encoding, errors=errors)
	cooked_string = raw_bytes.decode(encoding, errors=errors)

	print(raw_bytes, "<===>", cooked_string)

# opening the languages.txt file and encoding with utf-8 encoding
languages = open("languages.txt", encoding="utf-8")

# runs the main function with all the correct parameters and kick starts the loop.  
main(languages, input_encoding, error) 
