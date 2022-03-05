#8-1
def display_message():
    print('We are learning about functions')
display_message()

#8-2
def favorite_book(title):
    print(f"One of my favorite books is {title.title()}")
favorite_book('War and Peace')

#8-3
def make_shirt(size = 'L', message = 'I Love Python'):
    print(f"You have ordered a {size.title()} with the text: {message.upper()}.")
make_shirt('L', 'usa')
make_shirt(message = 'i like to code', size = 'm')

#8-4
make_shirt()
make_shirt('M')
make_shirt('S', 'deadlift')

#8-5
def describe_city(city, country = 'Mongolia'):
    print(f"{city.title()} is in {country.title()}")
describe_city('ulaAnbatAr')

#8-6
def city_country(city, country):
    print(f"{city.title()}, {country.title()}")
city_country('santiago','chILE')

#8-7
def make_album(artist_name, album_title = None, song_count = None):
    music = {artist_name: {album_title: song_count}}
    return music
print(make_album('Adele', '21'))
print(make_album('Rolling Stones', 'Gimme Shelter', '12'))

#8-8
while True:

    name = input('Name of artist ')
    if name == 'q':
        break
    title = input('Name of album ')
    if title == 'q':
        break
    count = input('How many songs are there? ')
    if count == 'q':
        break  
    final = make_album(name, title, count)
    print(final)

#8-9
messages = ['hi', 'how are you', 'bye bye']
send_messages = []
def message_sender(messages, send_messages):
    messages.reverse()
    while messages:
        current_message = messages.pop()
        send_messages.append(current_message)
    for x in send_messages:
        print(x)

message_sender(messages[:], send_messages)

#8-10
print(messages)
print(send_messages)

#8-11
#8-12
def sandwichmaker(*ingredients):
    print(f"The following ingredients will be added to the sandwich: ")
    for ingredient in ingredients:
        print(ingredient)
sandwichmaker('bacon', 'ham','cheese')

#8-13
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Jip', 'Snelder', location = 'Netherlands', field = 'Law')
print(user_profile)

#8-14
def car_info(manufacturer, model, **arg):
    car_dict = {
        'manufacturer' : manufacturer.title(),
        'model' : model.title(),
        }
    for k, v in arg.items():
        car_dict[k] = v
        
    return car_dict
car = car_info('subaru', 'outback', color = 'blue', towpackage = True)
print(car)

#8-15
