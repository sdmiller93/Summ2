# Modules, Classes, and Objects

# There is a construct in python called a class that lets you structure your software in a particular way.

# get X from Y

# DICTIONARY STYLE:
	# mystuff = {'apple': "I AM APPLES!"}
	# print(mystuff['apple']
	# from apple get I AM APPLES 
	# with the key, apple, get the value associated with it. 

##############################################################################################################

def apple():
	print("I AM APPLES!")

# this is just a variable
tangerine = "Living reflection of a dream."

#############################################################################################################


# 1. mystuff['apple'] # get apple from dict
	# DICTIONARY: key = string & syntax = [key]

# 2. mystuff.apple() # get apple from the module
	# DICTIONARY: key = identifier & syntax = .key

# 3. mystuff.tangerine # just a variable

#############################################################################################################

# module: specialized dictionary that can store python code so you can access it with the . operator

# a class: a way to take a grouping of functions and data and place them inside a container so you can access them with the . operator

# create a class via:::

class MyStuff(object):

	def _init_(self):
		self.tangerine = "And now a thousand years in between."

	def apple(self):
		print("I AM CLASSY APPLES!")

# Mini module with MyStuff having an apple() function in it. 

# the _init_() function and use of self.tangerine for setting the tangerine instance variabe. 

# Why classes are used instead of modules: you can take this MyStuff class and use it to craft many of them and each one
	# won't interfere with each other. 

# When you import a module there is only one for the entire program unless you do some monster hacks. 


#############################################################################################################


# class = mini module, then there has to be an import but for classes:

# "instantiate" = 'create'

# when you instantiate a class you get an object. 

# you instantiate a class by calling the class like it's function, like so:

thing = MyStuff() # instantiate operation
thing.apple()
print(thing.tangerine)

# python looks for MyStuff() and sees it's a class you created
# crafts an empty object with all the functions you've specified in the class using def
# looks for a 'magic' _init_ function and if you have, it calls that function to initialize your newly created empty object. 
# in the MyStuff function _init_ you get an extra variable, self, (the empty object created for you)
# in this case, you set self.tangerine to a song lyric, you've initialized this object. 
# can take this new object and assign it to the thing variable
# uses the class as a blueprint for building a copy of that type of thing. 

# MORE HONESTLY:
	# classes are like blueprints or definitions for creating new mini-modules
	# instantiation is how you make one of these mini-modules and import it at the same time. 
	# instantiate means to create an object from the class
	# the resulting created mini-module is called an object, and you then assign it to a variable to work with it. 

#############################################################################################################

# THREE WAYS TO GET THINGS FROM THINGS:

# dict style
mystuff['apples']

# module style
mystuff.apples()
print(mystuff.tangerine)

# class style
thing = MyStuff()
thing.apples()
print(thing.tangerine)
