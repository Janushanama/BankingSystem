Banking System
- Banking System that allows users to create accounts, perform banking transactions, and manage their finances.
- This system provide following functionalities:
  1. Create Account 
  2. Login 
  3. Check Balance 
  4. Deposit Money
  5. Withdraw Money
  6. Display All Accounts
  7. Exit



Python Environment
- We need Python 3.9 to run this project. This project is created using PyCharm IDE, it will be better if we execute it in the same IDE.

Account class
- Each bank account will be an instance of this class.
- This class has method for Methods for logging, depositing, withdrawing, checking balance and displaying account info.


Bank Class
- This class manages multiple accounts, allowing for account creation and searching.


FileWriter Class
- This class manages account and transactions related detail insertion in file.
- We can pass folder where we want to insert the data.
- Currently, we are writing both files in [OutputFiles](src/OutputFiles) folder.


Util File
- This file has a method named get_random_account_number which helps to create random account number of given size.
- Currently, We are creating 4 digit account number.

Main File
- This file is for user interaction, A simple command-line interface to interact with the bank.