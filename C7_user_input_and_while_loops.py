#7-1
rental_car = input('What kind of car would you like to rent? ')
print(f"Let me see if I can find a {rental_car}")
#7-2
seating = input('How many people are in your dinner group? ')
seating = int(seating)
if seating > 8:
    print("you'll have to wait for a table")
else:
    print('the table is ready')
#7-3
ten = input("tell me a number ")
ten = int(ten)
if ten % 10 == 0:
    print("This is a multiple of 10")
else:
    print('this is not a multiple of 10')
#7-4
pizza_topping = ''
while True:
    pizza_topping= input('what topping would you like on your pizza?' )
    if pizza_topping == 'quit':
        break
    else:
        print(f"We will add {pizza_topping} to the pizza")

#7-5
age = input('Please, tell me your age ')
age = int(age)
if age < 3:
    print('the ticket is free')
elif age >= 3 and age<12:
    print('the ticket is 10 dollars')
else:
    print('the ticket is 15 dollars')

#7-6
#7-7
#7-8
sandwich_orders = ['ham', 'pastrami', 'cheese', 'italian','pastrami', 'pastrami', 'american', 'bacon-and-egg']
finished_sandwiches = []
print('We ran out of pastrami')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if current_sandwich == 'pastrami':
        continue
    else:    
        print(f"I made you a {current_sandwich} sandwich")
        finished_sandwiches.append(current_sandwich)
    
print(finished_sandwiches)
print(sandwich_orders)
#7-9 see above
#7-10
status = True
countries = []
while status:
    destination = input('Where do you want to go for your dream vacation?')
    if destination == 'quit':
        break
    countries.append(destination)

for country in countries:
    print(country)
