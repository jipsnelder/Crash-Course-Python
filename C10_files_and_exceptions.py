#10-1
with open('learning_python.txt') as file_object:
    content = file_object.read()
print(content)

with open('learning_python.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

with open('learning_python.txt') as file_object:
    texts = file_object.readlines()
for text in texts:
    print(text.rstrip())

#10-2
print(content.replace('cats', 'wolves'))

#10-3
guest = input('What is your name?')
with open('guest.txt', 'a') as guesttext:
    guesttext.write(f"{guest}\n")

#10-4
while True:
    name = input('What is your name?')
    with open('guest_book.txt', 'a') as guestbook:
        guestbook.write(f"{name.title()}\n")
    print(f"Welcome to the jungle, {name.title()}")
    break

#10-5 copy pasta
#10-6

while True:
    number_one = input('provide number one')
    number_two = input('provide number two')
    try:
        summation = int(number_one) + int(number_two)
    except ValueError:
        print('Please, just use numbers instead of letters')
        continue
    else:
        print(f"The sum of the two numbers is: {summation}")
        break

#10-7
#10-8
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print("\nReading file: " + filename)
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print("  Sorry, I can't find that file.")

#10-9 diy
#10-11
import json
favorite_number = input('What is you favorite number?')
filename = 'favorite_number.json'
with open(filename, 'w') as f:
    json.dump(favorite_number, f)
with open('favorite_number.json') as f:
    number = json.load(f)
print("I know your favorite number! It's " + str(number) + ".")

#10-12

