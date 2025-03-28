# # # Bank Accounts
# # step 1
# class BankAccount:
#     def __init__(self,initial_amount,account_name,account_number,):
#         self.balance = initial_amount
#         self.name = account_name
#         self.account_number = account_number
#         print(f"\n Account '{self.name}'created. \n Account Number = {self.account_number} \n Balance = ${self.balance} ")
        
# # step 2
# class BankAccount:
#     def __init__(self,initial_amount,account_name,account_number,):
#         self.balance = initial_amount
#         self.name = account_name
#         self.account_number = account_number
#         print(f"\n Account '{self.name}'created. \n Account Number = {self.account_number} \n Balance = ${self.balance:.2f} ")
   
#  # step 3 
class BankAccount:
    def __init__(self,initial_amount,account_name,account_number,):
        self.balance = initial_amount
        self.name = account_name
        self.account_number = account_number
        print(f"\n Account '{self.name}'created. \n Account Number = {self.account_number} \n Balance = ${self.balance:.2f} ")
        
    def get_balance(self):
        print(f"\n Account'{self.name}' \n Acount number = {self.account_number}\n balance = ${self.balance:.2f}")
    #update amount comment
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\n Deposit Cpomlete.")
        self.get_balance()