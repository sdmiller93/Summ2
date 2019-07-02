# IS-A, HAS-A, OBJECTS, AND CLASSES
# is-a = when you talk about objects and classes being related to each other by a class relationship.
# has-a = when you talk about objects and classes that are related only because they reference each other.

# replace each ###?? comment with a comment that says whether the next line is an is-a or has-a relationship and what that relationship is.


#############################################################################################################################################

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object)
	pass

## Dog is-s Animal
class Dog(Animal):
	
	def __init__(self, name):
		## Dog has-a name
		self.name = name

## Cat is-a animal
class Cat(Animal):

	def __init__(self, name)
		## Cat has-a name	
		self.name = name

## Person is-a object
class Person(object):

	def __init__(self, name):
		## Person has-a name
		self.name = name

	## Person has-a pet of some kind
	self.pet = None

## Person is-a employee
class Employee(Person)

	def __init__(self, name, salary):
		## ?? 
		super(Employee, self).__init__(name)
		##??
		self.salary = salary

## Fish is-a object
class Fish(object):
	pass

## Salmon is a fish
class Salmon(Fish):	
	pass

## Halibut is a fish
class Halibut(Fish):


## rover is-a dog
rover = Dog("Rover")

## satan is a cat
satan = Cat("Satan")

## Mary is a person
mary = Person("Mary")

## Mary has-a pet and is-a cat (satan)
mary.pet = satan

## Frank is-a employee of 120,000?
frank = Employee("Frank", 120000)

## Frank has-a pet, it is a dog (rover)
frank.pet = rover

## Flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## Harry is-a Halibut
harry = Halibut()


