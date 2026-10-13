# 📚 Library Management System

A console-based Library Management System developed using Python. This project helps manage books, library members, book issues, returns, and library statistics using JSON file storage.

## 🚀 Features

- Add, view, search, update, and delete books
- Register and view library members
- Issue books and process returns
- Track book availability and loan history
- Calculate overdue days and fines
- Display library statistics
- Store records persistently in JSON files
- Validate user input and handle common errors

## 🛠️ Technologies Used

- Python 3
- JSON
- `pathlib`
- `datetime`

## 📂 Project Structure

```text
library-management-system/
├── main.py
├── books.json
├── members.json
├── loans.json
└── README.md
```

## ⚙️ Installation and Setup

1. Install Python 3.
2. Clone or download this repository.
3. Open a terminal inside the project folder.
4. Run the application:

```bash
python3 main.py
```

On Windows, use `python main.py` if that is your Python command.

## 📖 How to Use

1. Select an option from the main menu.
2. Add books and register library members.
3. Issue available books using their book IDs and member IDs.
4. Return books using their loan IDs.
5. View loan history and library statistics.

## 📋 Library Rules

- Each book has a unique book ID.
- Each member has a unique member ID.
- A member can borrow up to three books at a time.
- The standard loan period is 14 days.
- The sample fine rate is ₹5 per overdue day.
- Books with active loans cannot be deleted.

## 💾 Data Storage

The project uses three JSON files:

- `books.json` — book details and inventory
- `members.json` — registered member details
- `loans.json` — issue and return records

The JSON files are created automatically when missing. Existing records are preserved when the application loads them.

## 🎯 Learning Objectives

This project demonstrates Python functions, loops, conditional statements, lists, dictionaries, file handling, JSON serialization, exception handling, date calculations, and basic CRUD operations.

## 🔮 Future Enhancements

- SQLite or MySQL database integration
- Graphical user interface using Tkinter
- Web interface using Flask or Django
- Login and role-based access control
- Book reservation functionality
- Automated overdue notifications
- Unit tests and reporting dashboards

## 👨‍💻 Author

**Kaveri Ayyappa**


Git Hub:https://github.com/Ayyappa1295


A Python project created for programming practice and portfolio development.

## 📄 License

This project is available for educational and learning purposes.
