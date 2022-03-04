#4-1
pizzas = ['quattro stagioni', 'calzone', 'marinara']
for pizza in pizzas:
	print(f"I like {pizza.title()} pizza")
print('I fucking hate pizza')
#4-2
animals = ['dog', 'cat', 'pikachu']
for animal in animals:
	print(animal.title())
print('These animal would make a great pet')
#4-3
counting = [count for count in range(1, 21)]
print(counting)
#could also take a normal for loop
numbers = []
for number in range(1,21):
	numbers.append(number)
print(numbers)
#4-4 I go to 10.000
tenthousand = [y for y in range(1, 10001)]
print(tenthousand)
#4-5
print(max(tenthousand))
print(min(tenthousand))
print(sum(tenthousand))
#4-6
odd_number = [odd for odd in range(1,21,2)]
print(odd_number)
#4-7
threes = [three*3 for three in range(1,31)]
print(threes)
#4-8
cubes = [cube**3 for cube in range(1,11)]
print(cubes)
#4-9 see above
#4-10
print(f"The first two items in this list are:")
for animal in animals[:2]:
	print(animal)
print(f"The item in the middle of this list is:")
for animal in animals[1:2]:
	print(animal)
print(f"The last items in this list is {animals[-1].title()}")
#4-11
friend_pizzas = pizzas[:]
friend_pizzas.append('pepperoni')
print(pizzas)
print(friend_pizzas)
#4-12 did it above.
#4-13
foods = ('rice', 'noodles', 'pork', 'vegetables', 'egg')
for food in foods:
	print(food)

foods = ('rice', 'potato', 'beef', 'vegetables', 'egg')
for food in foods:
	print(food)