class Saving:
    def __init__(self):
        super().__init__()
        self.balance = 50
        self.name = 'Saving'
    
    def make_deposit(self,amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if Saving.can_withdraw(self.balance, amount):
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
    def account_info(self):
        print(f"Account Name :{self.name} - Balance is :{self.balance}")
class Checking:
    def __init__(self):
        self.balance = 50
        self.name = 'Checking'
    def make_deposit(self,amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if Checking.can_withdraw(self.balance, amount):
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
    def account_info(self):
        print(f"Account Name :{self.name} - Balance is :{self.balance}")
class User:
    def __init__(self):
        self.name = 'Brian'
        self.saving = Saving()
        self.checking = Checking()
        
    def saving_account_info(self):
        self.saving.account_info()
    def saving_deposit(self,amount):
        self.saving.make_deposit(amount)
        return self
    def saving_withdraw(self,amount):
        self.saving.withdraw(amount)
        return self
    def checking_account_info(self):
        self.checking.account_info()
    def checking_deposit(self,amount):
        self.checking.make_deposit(amount)
        return self
    def checking_withdraw(self,amount):
        self.checking.withdraw(amount)
        return self
brian = User()
brian.checking_deposit(300).checking_deposit(200).checking_deposit(100).checking_withdraw(100).checking_account_info()
brian.saving_deposit(200).saving_deposit(200).saving_withdraw(50).saving_account_info()