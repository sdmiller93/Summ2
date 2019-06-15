# import argv module
from sys import argv

script, filename = argv

txt = open(filename)
print(f"Here is what your file says:")
print(txt.read())

txt.close()

