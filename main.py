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

    def withdraw(self, amount):
        self.amount = amount
        if self.amount> self.balance:
            print(f'Insufficient Funds | The available fund to withdraw is: ${self.balance}')
        else:
            self.balance = self.balance - self.amount
            print(f'The balance has beeen updated to ${self.balance}')

    def view_balance(self):
        self.show_details()
        print(f'Account Balance: ${self.balance}')
    



nischit = Bank('Nischit', 25, 'Male')
# nischit.show_details()
nischit.deposit(300)

nischit.deposit(700)
nischit.withdraw(450)
nischit.view_balance()
