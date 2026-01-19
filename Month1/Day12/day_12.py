# Day - 12 - > DEEP DIVE: Theory: The Blueprint (OOP)
print("Day 12: Deep Dive Exercises")



# DEEP DIVE - 1: Micro-Challenge: The Constructor
print("DEEP DIVE - 1: Micro-Challenge: The Constructor")

class User:
    def __init__(self, name):
        self.name = name
        self.is_active = True

user_obj = User("Jahid")
print(user_obj.name)
print(user_obj.is_active)
print()



# DEEP DIVE - 2: Micro-Challenge: The Self Reference
print("DEEP DIVE - 2: Micro-Challenge: The Self Reference")

class User:
    def greet(self):
        print("Hello,", self.name)
user_obj = User()
user_obj.name = "Jahid"
user_obj.greet()
print()



# DEEP DIVE: 3 - Micro-Challenge: The Inheritance
print("DEEP DIVE: 3 - Micro-Challenge: The Inheritance")

class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"User: {self.name}"

    def __repr__(self):
        return f"User(name='{self.name}')"
    
user_obj = User("Jahid")
print(str(user_obj))
print(repr(user_obj))
print()



# DEEP DIVE: 4 - Micro-Challenge: Private Variables
print("DEEP DIVE: 4 - Micro-Challenge: Private Variables")

class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password

user_obj = User("Jahid", "mypassword")
print("User Name:", user_obj._User__password)
try:
    print(user_obj.__password)
except AttributeError as e:
    print("Error:", e)
print()


# DEEP DIVE: 5 - Micro-Challenge: Property Decorator
print("DEEP DIVE: 5 - Micro-Challenge: Property Decorator")

from datetime import datetime

class User:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    @property
    def age(self):
        current_year = datetime.now().year
        return current_year - self.birth_year
user_obj = User("Jahid", 2002)
print(f"{user_obj.name} is {user_obj.age} years old.")
print()



# DEEP DIVE: 6 - Micro-Challenge: Class vs Instance Variables
print("DEEP DIVE: 6 - Micro-Challenge: Class vs Instance Variables")

class User:
    species = "Human"   # Class variable

    def __init__(self, name):
        self.name = name   # Instance variable

user1 = User("Jahid")
user2 = User("Alice")
print(user1.species)
print(user2.species)
User.species = "Alien"
print(user1.species)
print(user2.species)
print()

# DEEP DIVE: 7 - Micro-Challenge: Inheritance
print("DEEP DIVE: 7 - Micro-Challenge: Inheritance")

class Admin(User):
    def delete_db(self):
        print("Database deleted!")

admin_obj = Admin("Admin_Noor")
print(admin_obj.name)
admin_obj.delete_db()
print()



# DEEP DIVE: 8 - Micro-Challenge: The Super Proxy
print("DEEP DIVE: 8 - Micro-Challenge: The Super Proxy")

class Admin(User):
    def __init__(self, name, level):
        super().__init__(name)
        self.level = level
    def greet(self):
        super()
        print(f"Admin Level: {self.level}")

admin_obj = Admin("Admin_Noor", 5)
admin_obj.greet()
print()




# DEEP DIVE: 9 - Micro-Challenge: Operator Overloading
print("DEEP DIVE: 9 - Micro-Challenge: Operator Overloading")

class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return Wallet(self.balance + other.balance)

wallet1 = Wallet(100)
wallet2 = Wallet(150)
wallet3 = wallet1 + wallet2
print(f"Combined Wallet Balance: {wallet3.balance}")
print()





# DEEP DIVE: 10 - Micro-Challenge: Equality
print("DEEP DIVE: 10 - Micro-Challenge: Equality")

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __eq__(self, other):
        return self.user_id == other.user_id

user1 = User(1)
user2 = User(1)
user3 = User(2)
print(user1 == user2)
print(user1 == user3)
print()


print("Deep Dive Exercises for Day 12 are Finished.")
print()