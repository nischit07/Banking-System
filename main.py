#Parent Class
class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def show_details(self):
        print('Personal Details')
        print("")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f'Gender: {self.gender}')


#Child Class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name,age,gender)

        self.balance  = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print(f"The balance has been updated to ${self.balance}")



# nischit = User('Nischit', 25, 'Male')
# nischit.show_details()
# nischit.deposit(300)
