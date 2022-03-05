#6-1
person = {'first_name': 'Gordon', 'last_name': 'Ramsay', 'age': 55, 'city': 'London'}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

#6-2
favorite_numbers = {'kim': 8, 'laura': 9, 'robert': 2, 'john': 3, 'alex': 6}
print(f"Kim's favorite number is: {favorite_numbers['kim']}")

#6-3 not gonna do
#6-4
for k,v in favorite_numbers.items():
	print(f"{k.title()}'s favorite number is: {v}")

#6-5
rivers = {'nile': 'egypt', 'amazon': 'brazil', 'yangtze': 'china'}
for k,v in rivers.items():
	print(f"The {k.title()} runs through {v.title()}")
for k in rivers.keys():
	print(k)
for v in rivers.values():
	print(v)

#6-6
names = ['jen', 'sarah', 'ben', 'margo', 'zlatan','andy']
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python',}
for name in names:
	if name in favorite_languages.keys():
		print(f"Thank you for responding {name.title()}")
	else:
		print(f"Please take the poll {name.title()}")

#6-7
person1 = {'first_name': 'Gordon', 'last_name': 'Ramsay', 'age': 55, 'city': 'London'}
person2 = {'first_name': 'Jamie', 'last_name': 'Oliver', 'age': 49, 'city': 'Manchester'}
person3 = {'first_name': 'Uncle', 'last_name': 'Roger', 'age': 33, 'city': 'Singapore'}

people = [person1, person2, person3]

for person in people:
	print(person)

#6-8
#6-9
favorite_places = {'yani': ['shenzhen', 'guilin', 'newcastle'], 
	'andy': ['manchester', 'london', 'birmingham'], 
	'gary': ['madrid', 'valencia', 'barcelona'],}
for k,v in favorite_places.items():
	print(f"{k.title()}'s favorite places are:")
	for cities in v:
		print(f"\t{cities.title()}")

#6-10
favorite_numbers = {'kim': [8, 12, 14], 'laura': [1,2,3,9], 'robert': [2,123,124], 'john': [0,3], 'alex': [1,2,3,4,5,6]}
for k,v in favorite_numbers.items():
	print(f"{k.title()}'s favorite numbers are:")
	for number in v:
		print(f"\t{number}")

#6-11
city = {
	'amsterdam': {'country': 'netherlands', 'population': 1_000_000},
	'berlin': {'country': 'germany', 'population': 2_500_000},
	'vienna': {'country': 'austria', 'population': 800_000},
	}
for place, facts in city.items():
	print(f"{place.title()} is located in {facts['country'].title()} and has a population of {facts['population']}")

#6-12
for place, fact in city.items():
	print(f"Here are facts about: {place.title()}")
	print(f"\tCountry of origin: {fact['country'].title()}")
	print(f"\tPopulation: {fact['population']}")
