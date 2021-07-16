
class User:
    bank_name = "OnPoint"
    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.balance = balance
    def make_deposit(self, amount):
        # your code goes here...
        self.balance += amount
        return self
    def display_user_balance(self, name, balance):
        self.balance = f"User :{name} - Balance :{balance}"
        return self
    def withdraw_balance(self, amount):
        self.balance -= amount
        return self
    def transfer_balance(self, transfer, other_user):
        self.balance -= transfer
        other_user += transfer
        return self

brian = User("Brian" , "brianp@gmail.com", 0)
orestes = User("Orestes", "orestesm@gmail.com" , 0)
dariel = User("Dariel", "dariele@gmail.com" , 0)

brian.make_deposit(100).make_deposit(100).make_deposit(100).withdraw_balance(50).transfer_balance(50,dariel.balance).display_user_balance(brian.name, brian.balance)
print(brian.balance)
orestes.make_deposit(100).make_deposit(200).make_deposit(100).withdraw_balance(50).withdraw_balance(50).display_user_balance(orestes.name, orestes.balance)
print(orestes.balance)
dariel.make_deposit(100).make_deposit(100).make_deposit(100).withdraw_balance(200).display_user_balance(dariel.name, dariel.balance)
print(dariel.balance)
