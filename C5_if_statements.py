#5-1
number = 8
print(number == 9) #F
print(number > 6 and number < 10) #T
print(number > 4 or number > 10) #T
word = 'Glass'
print(word == 'Glass') #T
print(word == 'glass') #F
#5-2
car = 'Volkswagen'
print(car.lower() == 'volkswagen')
furniture = ['table', 'chair', 'lamp']
print('table' in furniture)
print('book' in furniture)
print('computer' not in furniture)
#5-3
#alien_color = ['green', 'yellow', 'red']
alien_color = 'green'
if alien_color == 'green':
	print('You just earned 5 points!')
if alien_color == 'yellow':
	print('You just earned 5 points!')

alien_color = 'red'
if alien_color == 'green':
	print('You just earned 5 points!')
elif alien_color != 'green':
	print('You just earned 10 points!')

if alien_color == 'green':
	print('You just earned 5 points!')
else:
	print('You just earned 10 points!')
#5-5
alien_color = 'red'
if alien_color == 'green':
	print('You just earned 5 points')
elif alien_color == 'yellow':
	print('You just earned 10 points')
else:
	print('You just earned 15 points!')

if alien_color == 'green':
	print('You just earned 5 points')
elif alien_color != 'red':
	print('You just earned 10 points')
else:
	print('You just earned 15 points!')

if alien_color == 'green':
	print('You just earned 5 points')
elif alien_color != 'red':
	print('You just earned 10 points')
elif alien_color == 'red':
	print('You just earned 15 points!')

#5-6
age = 25
if age < 2:
	print('baby')
elif age >= 2 and age < 4:
	print('toddler')
elif age >= 4 and age < 13:
	print('kid')
elif age >= 13 and age < 20:
	print('teenager')
elif age > 20 and age <65:
	print('adult')
elif age >= 65:
	print('elder')

#5-7
favorite_fruits = ['kiwi', 'banana', 'mango']
if 'banana' in favorite_fruits:
	fruit = 'banana'

print(f"You really like {fruit.upper()}")

#5-8
usernames = ['kate','peter', 'admin', 'walter', 'simon']
for username in usernames:
	if username == 'admin':
		print(f"Hello {username}, would you like to see a status report?")
	else:
		print(f"Hello {username.title()}, thank you for logging in.")

#5-9
no_users = [] #test with a name
if no_users:
	for no_user in no_users:
		print(f"Hi {no_user}")
else:
	print('there is no user')

#5-10
current_users = ['kate','peter', 'admin', 'walter', 'simon']
new_users = ['kate','DANIEL', 'frank', 'laura', 'SIMON']

new_users_lower = []
for new_user in new_users:
	new_users_lower.append(new_user.lower())

for new_user in new_users_lower:
	if new_user in current_users:
		print('Enter a new username')
	else:
		print('This username is available')
print(new_users_lower)

#5-11
ordinal_numbers = [*range(1,10)]
print(ordinal_numbers)
for number in ordinal_numbers:
	if number == 1:
		print('1st')
	elif number == 2:
		print('2nd')
	elif number == 3:
		print('3rd')
	else:
		print(f"{number}th")