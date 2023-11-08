from Bank_account import *

Harish = BankAccount(1000, "Harish")
Naren = BankAccount(2000, "Naren")

Harish.getBalance()
Naren.getBalance()

Harish.deposit(1500)

Harish.withdraw(10)

Harish.transfer(500, Naren)

Sugi = InterestRewardsAcct(1000, "Sugi")
Sugi.getBalance()
Sugi.deposit(200)
Sugi.transfer(150, Harish)

Rio = SavingsAcct(2000, "Rio")
Rio.getBalance()
Rio.deposit(250)
Rio.transfer(20000, Naren)
Rio.transfer(300, Naren)