class ATM:
    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.transactions = []

    def deposit(self, account, amount):
        account.current_balance += amount
        transaction = (
            f"[DEPOSIT] {account.account_firstname} {account.account_lastname} "
            f"added {amount} to their account. "
            f"Updated balance: {account.current_balance}."
        )
        print(transaction)
        self.transactions.append(transaction)

    def withdraw(self, account, amount):
        if account.current_balance >= amount:
            account.current_balance -= amount
            transaction = (
                f"[WITHDRAW] {account.account_firstname} {account.account_lastname} "
                f"took out {amount}. Remaining balance: {account.current_balance}."
            )
        else:
            transaction = (
                f"[FAILED WITHDRAW] {account.account_firstname} {account.account_lastname} "
                f"tried to withdraw {amount}, but only has {account.current_balance} available."
            )
        print(transaction)
        self.transactions.append(transaction)

    def check_current_balance(self, account):
        transaction = (
            f"[BALANCE CHECK] Account holder {account.account_firstname} "
            f"{account.account_lastname} currently has {account.current_balance} in their account."
        )
        print(transaction)
        self.transactions.append(transaction)

    def view_transactionsummary(self):
        print("\n--- Transaction Summary ---")
        if not self.transactions:
            print("No transactions have been recorded yet.")
        else:
            for i, t in enumerate(self.transactions, start=1):
                print(f"{i}. {t}")
        print(f"\nATM Serial Number: {self.serial_number}")
        print("Thank you for using this ATM. Have a great day!\n")

