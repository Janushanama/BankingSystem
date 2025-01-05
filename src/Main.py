from Bank import Bank
from Account import Account
from FileWriter import FileWriter
from Util import get_random_account_number

def main():
    bank = Bank()
    file_writer = FileWriter("./OutputFiles/")
    account_num_size = 4

    print("Welcome to the Banking System!")
    while True:
        choice = int(input("1. Create Account\n2. Login\n3. Check Balance\n4. Deposit Money\n"
                           "5. Withdraw Money\n6. Display All Accounts\n7. Exit\nEnter your choice: "))

        if choice == 1:
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter your initial deposit: "))

            account_number = get_random_account_number(account_num_size)

            print("Your account number: " + str(account_number) + " (Save this for login)")

            password = input("Enter a password: ")

            account_detail = bank.create_account(account_number, name, password, initial_deposit)
            file_writer.write_account_detail(account_detail)
        elif choice == 2:
            account_number = int(input('Enter your account number: '))
            password = input('Enter your password: ')
            account = bank.get_account(account_number)
            if account:
                account.login(password)
            else:
                print("Account number doesn't exist!")

        elif choice == 3:
            account_number = int(input('Enter your account number: '))
            account = bank.get_account(account_number)
            if account:
                print("You have " + str(account.get_balance()) + " amount in your account.")
            else:
                print("Account number doesn't exist!")

        elif choice == 4:
            account_number = int(input('Enter your account number: '))
            amount = float(input("Enter deposit amount: "))
            account = bank.get_account(account_number)
            if account:
                deposit_detail = account.deposit_amount(amount)
                if deposit_detail:
                    file_writer.write_transactions_detail(deposit_detail)
            else:
                print("Account number doesn't exist!")

        elif choice == 5:
            account_number = int(input('Enter your account number: '))
            amount = float(input("Enter withdrawal amount: "))
            account = bank.get_account(account_number)
            if account:
                withdrawal_detail = account.withdraw_amount(amount)
                if withdrawal_detail:
                    file_writer.write_transactions_detail(withdrawal_detail)
            else:
                print("Account number doesn't exist!")

        elif choice == 6:
            bank.display_all_accounts()

        elif choice == 7:
            print("Existing from the system")
            break


if __name__ == "__main__":
    main()