bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My favorite bike is a {bicycles[2].title()}"
print(message)

#3-1
names = ['jack','matthew','laura','thomas']
print(names[0])
print(names[1])
print(names[2])
print(names[-1].title())
#3-2
message = f"Nice to meet you, {names[0].title()}"
print(message)
#3-3
#see above
#3-4
guests = ['Putin','Biden','Xi']
print(f"Hi {guests[0].title()}, you're invited to the dinner")
print(f"Hi {guests[1].title()}, you're invited to the dinner")
print(f"Hi {guests[2].title()}, you're invited to the dinner")
#3-5
print(guests[-1])
guests[-1] = 'Jung-Un'
print(f"Hi {guests[2].title()}, you're invited to the dinner")
#3-6
print(f"Hi {guests[0]}, {guests[1]}, {guests[2]}, I have found a bigger dinner table!")
guests.insert(0, 'Merkel')
guests.insert(2, 'Trump')
guests.append('Confucius')
print(guests)
#copy paste for printing every message
#3-7
print('We only have place for two people at the dinner table')
removed_person = guests.pop()
print(f"Sorry {removed_person}, we cannot invite you this time")
removed_person = guests.pop()
print(f"Sorry {removed_person}, we cannot invite you this time")
removed_person = guests.pop(-1)
print(f"Sorry {removed_person}, we cannot invite you this time")
removed_person = guests.pop(-1)
print(f"Sorry {removed_person}, we cannot invite you this time")
print(f"Hi {guests[0]}, {guests[1]}, you're still invited!")
del guests[:]
print(guests)
#3-8
places = ['Seoul', 'Shanghai', 'Hong Kong', 'Chengdu','Singapore']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
#3-9
guests_new = ['Putin','Biden','Xi']
print(f"There are {len(guests_new)} people invited")
#3-10
#DIY
#3-11
#print(guests_new[4])