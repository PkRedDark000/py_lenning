# # # Bank Accounts
class BankAccount:
    def __init__(self,initial_amount,account_name,account_number,):
        self.balance = initial_amount
        self.name = account_name
        self.account_number = account_number
        print(f"\n Account '{self.name}'created. \n Account Number = {self.account_number} \n Balance = ${self.balance} ")
        