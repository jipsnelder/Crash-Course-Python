from C9_classes_restaurant import Restaurant, User, Admin, Privileges
from random import randint

#9-1
"""""
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"{self.restaurant_name} {self.cuisine_type}")
    
    def set_number_served(self, set_number):
        self.number_served = set_number###


    def increment_number_served(self, increment = 1):
        self.number_served += increment
"""""
my_restaurant = Restaurant('Taco pez', 'mexican')
my_restaurant.describe_restaurant()

#9-2
your_restaurant = Restaurant('Mcdonalds', 'American')
your_restaurant.describe_restaurant()
another_restaurant = Restaurant('Dolce vita', 'Italian')
another_restaurant.describe_restaurant()

#9-3
'''''
class User:
    def __init__(self, first_name, last_name, age, login_attempts = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = login_attempts
    
    def describe_user(self):
        print(f"{self.first_name}, {self.last_name}, {self.age}")

    def greet_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Hi {full_name}, how are you doing?")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

'''''
user1 = User('Jip', 'Snelder', '25')
user1.describe_user()
user1.greet_user()

#9-4
my_restaurant.number_served = 5
print(my_restaurant.number_served)
my_restaurant.set_number_served(15)
print(my_restaurant.number_served)
my_restaurant.increment_number_served(2)
print(my_restaurant.number_served)
my_restaurant.increment_number_served()
print(my_restaurant.number_served)

#9-5
user2 = User('William', 'Jones', '33')
print(user2.login_attempts)
user2.increment_login_attempts()
print(user2.login_attempts)
user2.increment_login_attempts()
print(user2.login_attempts)
user2.reset_login_attempts()
print(user2.login_attempts)

#9-6
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = []
    
    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor.title())

coldcone = IceCreamStand('Cold Cone', 'Ice Cream Stand')
coldcone.flavors = ['vanilla', 'citrus', 'chocolate']
coldcone.show_flavors()

#9-7
""""
class Admin(User):
    def __init__(self, first_name, last_name, age, login_attempts=0):
        super().__init__(first_name, last_name, age, login_attempts)
        self.privileges = []
    
    def show_privileges(self):
        print(f"These are your privileges:")
        for privilage in self.privileges:
            print(f"- {privilage}")

administrator = Admin('Louis', 'Van Gaal', 65)
administrator.privileges = ['can add post', 'can delete post', 'can delete user']
administrator.show_privileges()
"""
#9-8
""""
class Privileges:
    def __init__(self, privileges = []):
        self.privileges = privileges

    def show_privileges(self):
        print(f"These are your privileges:")
        for privilage in self.privileges:
            print(f"- {privilage}")

administrator2 = Admin('Ronald', 'Koeman', 58)
administrator2.privileges = ['can change post', 'can add post', 'can change user']
administrator2.show_privileges()
"""
#9-9
class Car():
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=60):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """Upgrade the battery if possible."""
        if self.battery_size == 60:
            self.battery_size = 85
            print("Upgraded the battery to 85 kWh.")
        else:
            print("The battery is already upgraded.")
    
        
class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


print("Make an electric car, and check the battery:")
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()

print("\nUpgrade the battery, and check it again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

print("\nTry upgrading the battery a second time.")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

#9-10
#9-13
class Dice:
    def __init__(self, sides = 6):
        self.sides = sides
    def roll_die(self):
        print(str(randint(1,self.sides)))

six_dice = Dice()
x = 0
while x < 10:
    six_dice.roll_die()
    x += 1

ten_dice = Dice(10)
x = 0
while x < 10:
    ten_dice.roll_die()
    x += 1
twenty_dice = Dice(20)
x = 0
while x < 10:
    twenty_dice.roll_die()
    x += 1

#9-14


