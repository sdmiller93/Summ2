# map cities and states/regions in my country

# create a mapping of state to abbreviation
states = {
	'Pennsylvania' = 'PA', 
	'Maryland' = 'MD', 
	'New York' = 'NY'
	'New Jersey' = 'NJ'
}

# create a basic set of states and some cities in them
cities - {
	'PA' = 'Harrisburg', 
	'MD' = 'Gaithersburg', 
	'NY' = 'Ithica'
} 

# add cities another way
cities['NJ'] = 'Trenton'

# print out a city
print('*' * 10)
print("Pennsylvania has: ", cities['PA'])

# print out a state
print("Maryland's abbreviation is: ", states['Maryland'])

# print using states then cities dict
print("New York has: ", cities[states['New Jersey']])

# print every state abbreviation
print('*' * 10)
for state, abbrev in list(cities.items()):
	print(f"{state} is abbreviated {abbrev}")
	print(f" and has city {cities[abbrev[}")
