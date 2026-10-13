
import json
from pathlib import Path
from datetime import date, timedelta

# ==========================================
# LIBRARY MANAGEMENT SYSTEM
# Language: Python
# Storage: JSON
# ==========================================

BASE_DIR = Path(__file__).resolve().parent

BOOKS_FILE = BASE_DIR / "books.json"
MEMBERS_FILE = BASE_DIR / "members.json"
LOANS_FILE = BASE_DIR / "loans.json"


# ---------- JSON FILE HANDLING ----------

def load_data(file_path):
    """Load records from a JSON file."""
    try:
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_data(file_path, data):
    """Save records to a JSON file."""
    try:
        with file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        return True
    except OSError as error:
        print(f"Error saving data: {error}")
        return False


def initialize_files():
    """Create the JSON files if they do not exist."""
    for file_path in (BOOKS_FILE, MEMBERS_FILE, LOANS_FILE):
        if not file_path.exists():
            save_data(file_path, [])


# ---------- COMMON HELPERS ----------

def get_next_id(records, field):
    """Generate the next numeric ID."""
    return max(
        (int(record.get(field, 0)) for record in records),
        default=0
    ) + 1


def get_non_empty(prompt):
    """Accept non-empty text."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Try again.")


def get_positive_int(prompt, minimum=1):
    """Accept a valid positive integer."""
    while True:
        try:
            value = int(input(prompt))
            if value >= minimum:
                return value
            print(f"Enter a number greater than or equal to {minimum}.")
        except ValueError:
            print("Please enter a valid whole number.")


def find_record(records, field, value):
    """Find a record by a field."""
    for record in records:
        if str(record.get(field, "")).lower() == str(value).lower():
            return record
    return None


# ---------- BOOK MANAGEMENT ----------

def display_book(book):
    print("-" * 55)
    print(f"Book ID       : {book['book_id']}")
    print(f"Title         : {book['title']}")
    print(f"Author        : {book['author']}")
    print(f"Category      : {book['category']}")
    print(f"ISBN          : {book['isbn']}")
    print(f"Total copies  : {book['total_copies']}")
    print(f"Available     : {book['available_copies']}")
    print("-" * 55)


def add_book():
    books = load_data(BOOKS_FILE)

    print("\n--- Add New Book ---")
    title = get_non_empty("Enter book title: ")
    author = get_non_empty("Enter author name: ")
    category = get_non_empty("Enter category: ")
    isbn = get_non_empty("Enter ISBN: ")

    if find_record(books, "isbn", isbn):
        print("A book with this ISBN already exists.")
        return

    copies = get_positive_int("Enter number of copies: ")

    book = {
        "book_id": get_next_id(books, "book_id"),
        "title": title,
        "author": author,
        "category": category,
        "isbn": isbn,
        "total_copies": copies,
        "available_copies": copies
    }

    books.append(book)

    if save_data(BOOKS_FILE, books):
        print(f"Book added successfully! Book ID: {book['book_id']}")


def view_books():
    books = load_data(BOOKS_FILE)

    print("\n--- All Books ---")
    if not books:
        print("No books found.")
        return

    for book in books:
        display_book(book)


def search_books():
    books = load_data(BOOKS_FILE)

    keyword = get_non_empty(
        "Search by title, author, category, ISBN or book ID: "
    ).lower()

    results = [
        book for book in books
        if keyword in str(book.get("title", "")).lower()
        or keyword in str(book.get("author", "")).lower()
        or keyword in str(book.get("category", "")).lower()
        or keyword in str(book.get("isbn", "")).lower()
        or keyword == str(book.get("book_id", "")).lower()
    ]

    if results:
        print(f"\nFound {len(results)} matching book(s).")
        for book in results:
            display_book(book)
    else:
        print("No matching books found.")


def update_book():
    books = load_data(BOOKS_FILE)
    book_id = get_positive_int("Enter book ID to update: ")
    book = find_record(books, "book_id", book_id)

    if not book:
        print("Book not found.")
        return

    display_book(book)
    print("Press Enter to keep the existing value.")

    for field in ("title", "author", "category", "isbn"):
        new_value = input(f"{field.title()} [{book[field]}]: ").strip()

        if new_value:
            if field == "isbn":
                duplicate = find_record(books, "isbn", new_value)
                if duplicate and duplicate["book_id"] != book_id:
                    print("Another book already uses this ISBN.")
                    return
            book[field] = new_value

    new_total = input(
        f"Total copies [{book['total_copies']}]: "
    ).strip()

    if new_total:
        try:
            new_total = int(new_total)
            borrowed = book["total_copies"] - book["available_copies"]

            if new_total < borrowed or new_total < 0:
                print("Total copies cannot be less than copies on loan.")
                return

            book["total_copies"] = new_total
            book["available_copies"] = new_total - borrowed
        except ValueError:
            print("Invalid number of copies.")
            return

    if save_data(BOOKS_FILE, books):
        print("Book updated successfully.")


def delete_book():
    books = load_data(BOOKS_FILE)
    loans = load_data(LOANS_FILE)

    book_id = get_positive_int("Enter book ID to delete: ")
    book = find_record(books, "book_id", book_id)

    if not book:
        print("Book not found.")
        return

    active_loans = [
        loan for loan in loans
        if loan["book_id"] == book_id and loan["status"] == "Issued"
    ]

    if active_loans:
        print("Cannot delete a book that has active loans.")
        return

    confirm = input(
        f"Delete '{book['title']}'? (yes/no): "
    ).strip().lower()

    if confirm != "yes":
        print("Deletion cancelled.")
        return

    updated_books = [
        item for item in books if item["book_id"] != book_id
    ]

    if save_data(BOOKS_FILE, updated_books):
        print("Book deleted successfully.")


# ---------- MEMBER MANAGEMENT ----------

def register_member():
    members = load_data(MEMBERS_FILE)

    print("\n--- Register Library Member ---")
    name = get_non_empty("Enter member name: ")
    phone = get_non_empty("Enter phone number: ")
    email = get_non_empty("Enter email address: ")

    if find_record(members, "phone", phone):
        print("This phone number is already registered.")
        return

    member = {
        "member_id": get_next_id(members, "member_id"),
        "name": name,
        "phone": phone,
        "email": email,
        "joined_on": date.today().isoformat()
    }

    members.append(member)

    if save_data(MEMBERS_FILE, members):
        print(
            f"Member registered successfully! "
            f"Member ID: {member['member_id']}"
        )


def view_members():
    members = load_data(MEMBERS_FILE)

    print("\n--- Registered Members ---")
    if not members:
        print("No members registered.")
        return

    for member in members:
        print("-" * 45)
        print(f"Member ID : {member['member_id']}")
        print(f"Name      : {member['name']}")
        print(f"Phone     : {member['phone']}")
        print(f"Email     : {member['email']}")
        print(f"Joined    : {member['joined_on']}")
    print("-" * 45)


# ---------- ISSUE BOOK ----------

def issue_book():
    books = load_data(BOOKS_FILE)
    members = load_data(MEMBERS_FILE)
    loans = load_data(LOANS_FILE)

    print("\n--- Issue a Book ---")
    book_id = get_positive_int("Enter book ID: ")
    member_id = get_positive_int("Enter member ID: ")

    book = find_record(books, "book_id", book_id)
    member = find_record(members, "member_id", member_id)

    if not book:
        print("Book not found.")
        return

    if not member:
        print("Member not found. Register the member first.")
        return

    if book["available_copies"] <= 0:
        print("No copies of this book are currently available.")
        return

    active_count = sum(
        1 for loan in loans
        if loan["member_id"] == member_id
        and loan["status"] == "Issued"
    )

    if active_count >= 3:
        print("A member can borrow a maximum of 3 books.")
        return

    issue_date = date.today()
    due_date = issue_date + timedelta(days=14)

    loan = {
        "loan_id": get_next_id(loans, "loan_id"),
        "book_id": book_id,
        "member_id": member_id,
        "issue_date": issue_date.isoformat(),
        "due_date": due_date.isoformat(),
        "return_date": None,
        "status": "Issued"
    }

    book["available_copies"] -= 1
    loans.append(loan)

    # Save the updated book inventory and loan record.
    if not save_data(BOOKS_FILE, books):
        return

    if not save_data(LOANS_FILE, loans):
        # Roll back the inventory change if loan saving fails.
        book["available_copies"] += 1
        save_data(BOOKS_FILE, books)
        return

    print("Book issued successfully!")
    print(f"Book       : {book['title']}")
    print(f"Member     : {member['name']}")
    print(f"Issue date : {loan['issue_date']}")
    print(f"Due date   : {loan['due_date']}")


# ---------- RETURN BOOK ----------

def return_book():
    loans = load_data(LOANS_FILE)
    books = load_data(BOOKS_FILE)

    print("\n--- Return a Book ---")
    loan_id = get_positive_int("Enter loan ID: ")

    loan = find_record(loans, "loan_id", loan_id)

    if not loan or loan["status"] != "Issued":
        print("Active loan not found. Check the loan ID.")
        return

    book = find_record(books, "book_id", loan["book_id"])

    if not book:
        print("Book record not found. Contact the administrator.")
        return

    return_date = date.today()
    due_date = date.fromisoformat(loan["due_date"])
    overdue_days = max(0, (return_date - due_date).days)
    fine = overdue_days * 5

    loan["status"] = "Returned"
    loan["return_date"] = return_date.isoformat()
    loan["overdue_days"] = overdue_days
    loan["fine"] = fine

    book["available_copies"] += 1

    if not save_data(LOANS_FILE, loans):
        return

    if not save_data(BOOKS_FILE, books):
        print("Warning: Loan saved, but inventory saving failed.")
        print("Please check the book inventory before further transactions.")
        return

    print("Book returned successfully!")
    print(f"Return date : {return_date.isoformat()}")
    print(f"Overdue days: {overdue_days}")
    print(f"Fine        : Rs. {fine}")


# ---------- LOAN REPORTS ----------

def view_loans():
    loans = load_data(LOANS_FILE)
    books = load_data(BOOKS_FILE)
    members = load_data(MEMBERS_FILE)

    print("\n--- Loan History ---")

    if not loans:
        print("No loan records found.")
        return

    for loan in loans:
        book = find_record(books, "book_id", loan["book_id"])
        member = find_record(members, "member_id", loan["member_id"])

        book_title = book["title"] if book else "Deleted book"
        member_name = member["name"] if member else "Unknown member"

        print("-" * 50)
        print(f"Loan ID    : {loan['loan_id']}")
        print(f"Book       : {book_title}")
        print(f"Member     : {member_name}")
        print(f"Issue date : {loan['issue_date']}")
        print(f"Due date   : {loan['due_date']}")
        print(f"Status     : {loan['status']}")
        print(f"Return date: {loan.get('return_date') or 'Not returned'}")
        if loan["status"] == "Issued":
            overdue = max(
                0,
                (date.today() - date.fromisoformat(loan["due_date"])).days
            )
            print(f"Currently overdue days: {overdue}")
        else:
            print(f"Fine       : Rs. {loan.get('fine', 0)}")


def library_statistics():
    books = load_data(BOOKS_FILE)
    members = load_data(MEMBERS_FILE)
    loans = load_data(LOANS_FILE)

    total_titles = len(books)
    total_copies = sum(book["total_copies"] for book in books)
    available = sum(book["available_copies"] for book in books)
    issued = sum(
        1 for loan in loans if loan["status"] == "Issued"
    )
    returned = sum(
        1 for loan in loans if loan["status"] == "Returned"
    )
    overdue = sum(
        1 for loan in loans
        if loan["status"] == "Issued"
        and date.today() > date.fromisoformat(loan["due_date"])
    )
    total_fines = sum(loan.get("fine", 0) for loan in loans)

    print("\n========== LIBRARY STATISTICS ==========")
    print(f"Unique book titles : {total_titles}")
    print(f"Total book copies  : {total_copies}")
    print(f"Available copies   : {available}")
    print(f"Registered members : {len(members)}")
    print(f"Active loans       : {issued}")
    print(f"Returned loans     : {returned}")
    print(f"Overdue loans      : {overdue}")
    print(f"Recorded fines     : Rs. {total_fines}")
    print("========================================")


# ---------- MAIN MENU ----------

def main():
    initialize_files()

    while True:
        print("\n" + "=" * 45)
        print("       LIBRARY MANAGEMENT SYSTEM")
        print("=" * 45)
        print("1.  Add Book")
        print("2.  View All Books")
        print("3.  Search Books")
        print("4.  Update Book")
        print("5.  Delete Book")
        print("6.  Register Member")
        print("7.  View Members")
        print("8.  Issue Book")
        print("9.  Return Book")
        print("10. View Loan History")
        print("11. Library Statistics")
        print("0.  Exit")
        print("=" * 45)

        choice = input("Enter your choice: ").strip()

        actions = {
            "1": add_book,
            "2": view_books,
            "3": search_books,
            "4": update_book,
            "5": delete_book,
            "6": register_member,
            "7": view_members,
            "8": issue_book,
            "9": return_book,
            "10": view_loans,
            "11": library_statistics
        }

        if choice == "0":
            print("Thank you for using the Library Management System!")
            break

        action = actions.get(choice)

        if action:
            try:
                action()
            except (KeyError, TypeError) as error:
                print(f"Data error: {error}")
                print("Check the JSON files for invalid or missing fields.")
            except (ValueError, OverflowError) as error:
                print(f"Invalid data: {error}")
        else:
            print("Invalid choice. Please select a valid menu option.")


if __name__ == "__main__":
    main()
