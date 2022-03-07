class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"{self.restaurant_name} {self.cuisine_type}")
    
    def set_number_served(self, set_number):
        self.number_served = set_number

    def increment_number_served(self, increment = 1):
        self.number_served += increment
    

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

class Admin(User):
    def __init__(self, first_name, last_name, age, login_attempts=0):
        super().__init__(first_name, last_name, age, login_attempts)
        self.privileges = []
    
    def show_privileges(self):
        print(f"These are your privileges:")
        for privilage in self.privileges:
            print(f"- {privilage}")

class Privileges:
    def __init__(self, privileges = []):
        self.privileges = privileges

    def show_privileges(self):
        print(f"These are your privileges:")
        for privilage in self.privileges:
            print(f"- {privilage}")