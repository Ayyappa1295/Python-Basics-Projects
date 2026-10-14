# 🏦 ATM Banking System Using Python

## 📌 Project Overview

The ATM Banking System is a console-based banking application developed using Python. It simulates basic ATM operations, allowing users to log in using an account number and PIN, check their balance, deposit money, withdraw cash, view transaction history, and change their ATM PIN.

Account information and transaction records are stored in a JSON file, allowing data to persist between program executions.

## ✨ Features

- 🔐 Account login with PIN verification
- 💰 Balance enquiry
- 💵 Cash deposit
- 💳 Cash withdrawal with balance validation
- 📜 Mini statement showing the 10 most recent transactions
- 🔑 ATM PIN change with confirmation
- 💾 Persistent storage using JSON
- 🚪 Logout and exit options
- ⚠️ Input validation and error handling
- 🔄 Support for multiple sample accounts

## 🛠️ Technologies Used

- **Language:** Python 3
- **Data Storage:** JSON
- **Concepts:** Functions, loops, conditional statements, dictionaries, lists, exception handling, file handling, and date/time operations

## 📂 Project Structure

```text
ATM-Banking-System/
├── main.py
├── accounts.json
└── README.md
```

## 🚀 Installation and Execution

### Prerequisites

- Python 3 installed on your computer
- Any Python editor, such as VS Code, PyCharm, or IDLE

### Steps

1. Clone or download this repository.
2. Open the project folder in your terminal.
3. Run the application:

```bash
python3 main.py
```

4. Select the Login option.
5. Enter one of the sample account credentials.

## 🧪 Sample Login Credentials

| Account Number | PIN | Initial Balance |
|---|---|---:|
| 1001 | 1234 | Rs. 10,000 |
| 1002 | 5678 | Rs. 5,000 |

These are demonstration credentials for local testing only.

## 📋 ATM Menu

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Mini Statement
5. Change ATM PIN
6. Logout

## 💡 Learning Outcomes

This project demonstrates how to:

- Build a menu-driven Python application
- Organize code using reusable functions
- Validate user input
- Handle invalid inputs and file errors
- Read and write JSON data
- Maintain transaction records
- Implement basic account operations

## 🔮 Future Enhancements

- Graphical user interface using Tkinter
- Database integration using SQLite or MySQL
- Fund transfers between accounts
- Daily withdrawal limits
- Improved authentication and account locking
- Unit testing and automated test cases
- Password/PIN hashing and secure storage

## ⚠️ Disclaimer

This is an educational project intended for learning and demonstration purposes. It is not a production-ready banking application. PINs are stored in plain text, and the application does not implement real bank authentication, concurrent transaction controls, or production-grade security.

## 👨‍💻 Author

**Kaveri Ayyappa**

Git Hub: https://github.com/Ayyappa1295

Python Project | Beginner to Intermediate Level

---

⭐ If you find this project useful, consider starring the repository!
