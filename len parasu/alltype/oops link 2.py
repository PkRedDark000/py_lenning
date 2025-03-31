from oops_Project import *

Parasu = BankAccount(1000,"PARASU",123456789)
balachandra = BankAccount(10000,"Balachandra",237628798)
suresh = BankAccount(50000,"Suresh",5678387986)

balachandra.get_balance()
Parasu.deposit(1000)
Parasu.deposit(250.5)
suresh.Withdraw(45000)
suresh.Withdraw(200)
balachandra.transfer(2000,Parasu)