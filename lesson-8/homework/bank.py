import os

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
    def __str__(self):
        return f"Account Number: {self.account_number}, Name: {self.name}, Balance: {self.balance}"
    
class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()
    
    def create_account(self, name, initial_deposit):
        account_number = self._generate_account_number()
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        self.save_to_file()
        print(f"Account created successfully! Account Number: {account_number}")
    
    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(account)
        else: 
            print("Account not found!")
    
    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if amount > 0:
                account.balance +=amount
                self.save_to_file()
                print(f"Successfully deposited! New balance: {account.balance}")
            else:
                print("Invalid deposit amount")
        else: 
            print("Account not found")                
    
    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if amount > 0 and amount <= account.balance:
                account.balance -=amount
                self.save_to_file()
                print(f"Successfully withdrawn! New balance: {account.balance}")
            else:
                print("Invalid withdrawal amount or insufficient balance")
        else: 
            print("Account not found") 

    def save_to_file(self):
        if os.path.exists("accounts.txt"):
            with open("accounts.txt", 'w') as file:
                for account in self.accounts.values():
                    file.write(f"{account.account_number},{account.name},{account.balance}\n")
                    
    def load_from_file(self):
        if os.path.exists("accounts.txt"):
            with open("accounts.txt") as file:
                for line in file:
                    account_number, name, balance = line.strip().split(",")
                    self.accounts[account_number] = Account(account_number, name, float(balance))
    
    def _generate_account_number(self):
        return str(len(self.accounts)+1).zfill(6) 
    
def display_menu():
    print("\nWelcome to the Bank Application!")
    print("1. Create Account")
    print("2. View Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Exit")  
    
def main():
    bank = Bank()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit amount: "))
            bank.create_account(name, initial_deposit)

        elif choice == "2":
            account_number = input("Enter your account number: ")
            bank.view_account(account_number)

        elif choice == "3":
            account_number = input("Enter your account number: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit(account_number, amount)

        elif choice == "4":
            account_number = input("Enter your account number: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(account_number, amount)

        elif choice == "5":
            print("Thank you for using the Bank Application. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")         
            
main()               