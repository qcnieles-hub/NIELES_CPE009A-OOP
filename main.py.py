"""
main.py
"""

import Accounts
import ATM

# --- Create Account 1 ---
account1 = Accounts.Account()
account1.account_firstname = "Sassy"
account1.account_lastname = "McsideEye"
account1.current_balance = 2000
account1.address = "Dao Tobias, Fornier Antique, Philippines"
account1.email = "sassymc@gmail.com"

# --- Create Account 2 ---
account2 = Accounts.Account()
account2.account_firstname = "Angkol"
account2.account_lastname = "Toni"
account2.current_balance = 3000
account2.address = "Quezon City, Manila, Philippines"
account2.email = "angkoltoni@gmail.com"

# --- Create ATM with serial number ---
atm1 = ATM.ATM(serial_number=123456789)

# Transactions
atm1.deposit(account1, 500)
atm1.check_current_balance(account1)

atm1.deposit(account2, 300)
atm1.check_current_balance(account2)

# Show ATM serial number
print(f"\nATM Serial Number: {atm1.serial_number}")

# Show transaction summary
atm1.view_transactionsummary()
