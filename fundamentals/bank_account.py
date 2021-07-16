class BankAccount:
    bank_name = "OnPoint"
    all_accounts = []
# don't forget to add some default values for these parameters!
    def __init__(self, int_rate = 0.13, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    @classmethod 
    def sum_all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return f"Total Balance :{sum}"

# your code here! (remember, instance attributes go here)
# don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
# your code here
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
        else: 
            print('Insuficient Funds')
        return self
    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) >= 0:
            return True
        else:
            return False
# your code here
    def display_account_info(self):
        print(f"Balance is :{self.balance}")
# your code here
    def yield_interest(self):
        mult = self.balance
        if self.balance >= 0:
            mult *= self.int_rate
            self.balance += mult
            return self
# your code here

account = BankAccount()
account_saving = BankAccount(0.2,0)
account.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest().display_account_info()
account_saving.deposit(200).deposit(210).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()
print(BankAccount.sum_all_balances())