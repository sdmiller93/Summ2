# Symbol Review


################################################################################################################
# KEYWORD 	DESCRIPTION	 					EXAMPLE

 as 		part of the with-as statement.				with X as Y: pass

assert		Assert (ensure) that something is true. 		assert False, "Error!"

break		Stop this loop right now.				while True: continue

class 		define a class.						class Person(object)

continue	don't process more of the loop, do it again. 		while True: continue

del		delete from dictionary					del X[Y]

except		if an exception happens, do this. 			except ValueError as e: print(e)

exec		Run a string as Python					exec 'print("hello")'

finally		exceptions or not, finally do this no matter what.	finally: pass

global		declare taht you want a global variable			global X

is 		like == to test equality.				1 is 1 == True

lambda		create a short anonymous function			s = lambda y: y ** y; s(3)

pass		this block is empty.					def empty(): pass

raise		raise an exception when things go wrong			raise ValueError("No")

try 		try this block, and if exception, go to except.		try: pass

with 		with an expression as a variable do			with X as Y: pass

yield 		pause here and return to caller				def X() : yield Y; X() .next()



###########################################################################################################

# DATA TYPES

# TYPE		DESCRIPTION						EXAMPLE

floats 		stores decimals 					i = 10.389

dicts		stores a key=value mapping of things			e = {'x': 1, 'y': 2}

##########################################################################################################

# STRING ESCAPE SEQUENCES

# ESCAPE 	DESCRIPTION

\' 		single-quote

\"		double-quote

\a 		bell

\b 		backspace

\f		formfeed

\r		carriage

\v 		vertical tag

##########################################################################################################

# OPERATORS

# OPERATOR	DESCRIPTION					EXAMPLE

**		power of					2 ** 4 == 16

// 		floor division					2 // 4 == 0

%		string interpole or modulus			2 % 4 == 2

+= 		add and assign					x = 1; x += 2

-=		subtract and assign				x = 1; x -= 2

*= 		multiply and assign				x = 1; x *= 2

/= 		divide and assign				x = 1; x /= 2

//=		floor divide and assign				x = 1; x //= 2

%=		modulus assign					x = 1; x %= 2

**= 		power assign					x = 1; x **= 2


