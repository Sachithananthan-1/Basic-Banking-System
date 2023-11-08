class BalanceException(Exception):
    pass
class BankAccount:
    def __init__(self,initialAmt,acc_name):
        self.balance = initialAmt
        self.name = acc_name
        print(f"\nAccount '{self.name}' created. \nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"\nAmount is deposited. \nNew Balance, '{self.name}' = ${self.balance}")

    def viableTransaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of {self.balance:.2f}")

    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print('\nWithdraw complete')
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted : {error}")

    def transfer(self,amount,account):
        try:
            print("\n*********\nBeginning Transfer...")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransferred Successfully...\n**********")
        except BalanceException as error:
            print(f"Transferred Interupted. {error}")

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance +(amount * 1.05)
        print("Deposit Complete.")
        self.getBalance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self,initialAmt,acc_name):
        super().__init__(initialAmt,acc_name)
        self.fee = 5
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount+self.fee)
            self.balance  = self.balance  - (amount + self.fee)
            print("Withdraw Completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"Withdraw Interupted: {error}")