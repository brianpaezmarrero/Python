# If you've been following along, you're going to utilize the User class we've been discussing for this assignment.
class User:
    bank_name = "OnPoint"
    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.balance = balance
    def make_deposit(self, amount):
        self.balance += amount
    def withdraw_balance(self, amount):
        self.balance -= amount
    def display_user_balance(self, name, balance):
        self.balance = f"User: {name} - Balance: {balance}" 
    def transfer_balance(self,transfer,other_user):
        self.balance -= transfer
        other_user += transfer
# For this assignment, we'll add some functionality to the User class:
brian = User("Brian" , "brianp@gmail.com", 0)
orestes = User("Orestes", "orestesm@gmail.com" , 0)
dariel = User("Dariel", "dariele@gmail.com" , 0)
# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
brian.make_deposit(100)
brian.make_deposit(100)
brian.make_deposit(100)
brian.withdraw_balance(50)
brian.transfer_balance(50,dariel.balance)
orestes.make_deposit(200)
orestes.make_deposit(200)
orestes.withdraw_balance(50)
orestes.withdraw_balance(50)
dariel.make_deposit(200)
dariel.withdraw_balance(50)
dariel.withdraw_balance(50)
dariel.withdraw_balance(50)

brian.display_user_balance(brian.name, brian.balance)
orestes.display_user_balance(orestes.name, orestes.balance)
dariel.display_user_balance(dariel.name, dariel.balance)
print(brian.balance)
print(orestes.balance)
print(dariel.balance)



# display_user_balance(self) - have this method print the user's name and account balance to the terminal

# eg. "User: Guido van Rossum, Balance: $150