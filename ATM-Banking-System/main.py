
import json
import os
from datetime import datetime

DATA_FILE = "accounts.json"


def load_accounts():
    """Load account information from the JSON file."""
    if not os.path.exists(DATA_FILE):
        print("Error: accounts.json file not found.")
        return {}

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Error: Unable to read account data.")
        return {}


def save_accounts(accounts):
    """Save account information to the JSON file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(accounts, file, indent=4)
        return True
    except OSError:
        print("Error: Unable to save account data.")
        return False


def record_transaction(account, transaction_type, amount):
    """Add a transaction to the account history."""
    transaction = {
        "type": transaction_type,
        "amount": amount,
        "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }

    account["transactions"].append(transaction)


def get_amount(message):
    """Read and validate a positive whole-number amount."""
    try:
        amount = int(input(message))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return None

        return amount

    except ValueError:
        print("Please enter a valid whole number.")
        return None


def check_balance(account):
    print("\n========== ACCOUNT BALANCE ==========")
    print(f"Account Holder : {account['name']}")
    print(f"Available Balance: Rs. {account['balance']}")
    print("=====================================")


def deposit_money(account, accounts):
    print("\n========== CASH DEPOSIT ==========")
    amount = get_amount("Enter deposit amount: Rs. ")

    if amount is None:
        return

    account["balance"] += amount
    record_transaction(account, "Deposit", amount)

    if save_accounts(accounts):
        print(f"Rs. {amount} deposited successfully!")
        print(f"New Balance: Rs. {account['balance']}")
    else:
        account["balance"] -= amount
        account["transactions"].pop()
        print("Deposit could not be saved. Please try again.")


def withdraw_money(account, accounts):
    print("\n========== CASH WITHDRAWAL ==========")
    amount = get_amount("Enter withdrawal amount: Rs. ")

    if amount is None:
        return

    if amount > account["balance"]:
        print("Transaction failed: Insufficient balance.")
        return

    account["balance"] -= amount
    record_transaction(account, "Withdrawal", amount)

    if save_accounts(accounts):
        print(f"Please collect your Rs. {amount} cash.")
        print(f"Remaining Balance: Rs. {account['balance']}")
    else:
        account["balance"] += amount
        account["transactions"].pop()
        print("Withdrawal could not be saved. Please try again.")


def mini_statement(account):
    print("\n========== MINI STATEMENT ==========")
    print(f"Account Holder: {account['name']}")
    print(f"Current Balance: Rs. {account['balance']}")

    transactions = account["transactions"]

    if not transactions:
        print("No transactions available.")
        return

    print("\nRecent Transactions:")

    for transaction in reversed(transactions[-10:]):
        print(
            f"{transaction['date']} | "
            f"{transaction['type']} | "
            f"Rs. {transaction['amount']}"
        )

    print("====================================")


def change_pin(account, accounts):
    print("\n========== CHANGE ATM PIN ==========")

    old_pin = input("Enter current PIN: ")

    if old_pin != account["pin"]:
        print("Incorrect current PIN.")
        return

    new_pin = input("Enter new 4-digit PIN: ")

    if not (new_pin.isdigit() and len(new_pin) == 4):
        print("PIN must contain exactly 4 digits.")
        return

    confirm_pin = input("Confirm new PIN: ")

    if new_pin != confirm_pin:
        print("PINs do not match.")
        return

    old_value = account["pin"]
    account["pin"] = new_pin

    if save_accounts(accounts):
        print("ATM PIN changed successfully!")
    else:
        account["pin"] = old_value
        print("PIN change could not be saved.")


def atm_menu(account, accounts):
    while True:
        print("\n")
        print("*" * 42)
        print("          PYTHON ATM BANKING")
        print("*" * 42)
        print(f"Welcome, {account['name']}!")
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Mini Statement")
        print("5. Change ATM PIN")
        print("6. Logout")
        print("*" * 42)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            check_balance(account)

        elif choice == "2":
            deposit_money(account, accounts)

        elif choice == "3":
            withdraw_money(account, accounts)

        elif choice == "4":
            mini_statement(account)

        elif choice == "5":
            change_pin(account, accounts)

        elif choice == "6":
            print(f"Thank you, {account['name']}!")
            print("You have logged out successfully.")
            break

        else:
            print("Invalid choice. Please select 1-6.")


def login(accounts):
    print("\n========== ATM LOGIN ==========")
    account_number = input("Enter account number: ").strip()

    if account_number not in accounts:
        print("Account not found.")
        return

    account = accounts[account_number]

    # Allow up to 3 PIN attempts per login session.
    for attempt in range(3):
        pin = input("Enter your 4-digit ATM PIN: ")

        if pin == account["pin"]:
            print("\nLogin successful!")
            atm_menu(account, accounts)
            return

        remaining = 2 - attempt

        if remaining > 0:
            print(f"Incorrect PIN. Attempts remaining: {remaining}")

    print("Too many incorrect attempts. Please try again later.")


def main():
    accounts = load_accounts()

    if not accounts:
        print("No accounts loaded. Please check accounts.json.")
        return

    while True:
        print("\n" + "=" * 42)
        print("       WELCOME TO PYTHON ATM")
        print("=" * 42)
        print("1. Login")
        print("2. Exit")
        print("=" * 42)

        choice = input("Enter your choice (1-2): ").strip()

        if choice == "1":
            login(accounts)

        elif choice == "2":
            print("Thank you for using Python ATM Banking!")
            print("Have a nice day!")
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
