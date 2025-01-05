from datetime import date

class Account:
    def __init__(self, account_number, name, password, balance):
        self.account_number = account_number
        self.name = name
        self.password = password
        self.balance = balance

    def login(self, password):
        if password == self.password:
            print("Successfully logged in account " + str(self.account_number))
        else:
            print("Couldn't loging, password provided is incorrect")

    def deposit_amount(self, amount):
        if amount < 0:
            print("Deposit amount must be positive.")
        else:
            self.balance += amount
            print(f"{amount} deposited successfully into account " + str(self.account_number))
            return str(self.account_number) + "," + "Deposit" + "," + str(amount) + "," + str(date.today())
        return None


    def withdraw_amount(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance, you have only " + str(self.balance) + " in your account")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully from account " + str(self.account_number))
            return str(self.account_number) + "," + "Withdrawal" + "," + str(amount) + "," + str(date.today())
        return None

    def get_balance(self):
        return self.balance

    def display(self):
        print("Account Number: " + str(self.account_number))
        print("Name: " + str(self.name))
        print("Password: " + str(self.password))
        print("Balance: " + str(self.balance))


    def get_file_entry(self):
        return str(self.account_number) + "," + self.name + "," + self.password + "," + str(self.balance);