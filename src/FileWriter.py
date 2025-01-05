class FileWriter:
    def __init__(self, folder_path):
        self.account_files = open(folder_path + "/accounts.txt", "w")
        self.transactions_file = open(folder_path + "/transactions.txt", "w")
        self.add_headers()


    def add_headers(self):
        self.account_files.write("Account Number, Name, Password, Balance\n")
        self.transactions_file.write("Account Number, Transaction Type (Deposit/Withdrawal), Amount, Date\n")
        self.account_files.flush()
        self.transactions_file.flush()

    def write_account_detail(self, account_detail):
        self.account_files.write(account_detail + "\n")
        self.account_files.flush()

    def write_transactions_detail(self, transactions_detail):
        self.transactions_file.write(transactions_detail + "\n")
        self.transactions_file.flush()