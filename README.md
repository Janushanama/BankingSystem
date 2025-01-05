**Banking System**
- Banking System that allows users to create accounts, perform banking transactions, and manage their finances. It provides following functionalities:
  1. Create Account 
  2. Login 
  3. Check Balance 
  4. Deposit Money
  5. Withdraw Money
  6. Display All Accounts
  7. Exit


**Execution Environments**
- You need Python 3.9 to run this project. This project is created using PyCharm IDE, it will be better if you execute it in the same IDE.

**[Account](src/Account.py) Class**
- Each bank account will be an instance of this class.
- This class has methods for logging, depositing, withdrawing, checking balance and displaying account info.


**[Bank](src/Bank.py) Class**
- This class manages multiple accounts, allowing for account creation, searching and displaying all accounts.


**[FileWriter](src/FileWriter.py) Class**
- This class manages account and transactions related detail insertion in file.
- You can pass folder where you want to insert the data.
- Currently, I'm writing both files in [OutputFiles](src/OutputFiles) folder.


**[Util](src/Util.py) File**
- This python file has a method named *get_random_account_number* which helps to create random account number of given size.
- Currently, I'm creating 4 digits account number.

**[Main](src/Main.py) File**
- This python file is responsible for user interaction, a simple command-line interface to interact with the bank.