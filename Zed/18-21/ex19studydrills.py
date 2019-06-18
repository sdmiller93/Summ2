# this script is to reinforce this point: The variables in your function are not connected to the variables in your script.
# create the function cheese_and_crackers with define that takes two arguments: cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"You have {cheese_count} cheeses!")
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print("Man that's enough for a party!")
	print("Get a blanket. \n")

# give the function cheese_and_crackers the numbers for cheese_count and boxes_of_crackers directly.
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# Giving the variables amount_of_crackers and amount_of_cheese variables, script style.
print("OR, we can use variables from our script:")
amount_of_crackers = 10
amount_of_cheese = 50

# then giving the function the variables we created on the lines immediately previous
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# giving the function the numbers by doing math
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# and taking our variables script style then adding numbers to that.
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

