from Account import Account

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name, password, initial_deposit):
        self.accounts[account_number] = Account(account_number, name, password, initial_deposit)
        print("Account created successfully.")
        return str(account_number) + ", " + name + ", " + password + ", " + str(initial_deposit)


    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def display_all_accounts(self):
        if not self.accounts:
            print("No accounts in the bank.")
        else:
            for account in self.accounts.values():
                account.display()
                print("*" * 20)


