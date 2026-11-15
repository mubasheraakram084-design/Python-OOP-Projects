
import json
from pathlib import Path

from book import Book
from member import Member


class Library:

    def __init__(self):
        self.data_folder = Path(__file__).parent / "data"
        self.data_folder.mkdir(exist_ok=True)

        self.books_file = self.data_folder / "books.json"
        self.members_file = self.data_folder / "members.json"

        self.books = []
        self.members = []

        self.load_data()

    # ---------- FILE HANDLING ----------

    def load_data(self):
        if self.books_file.exists():
            with open(self.books_file, "r") as file:
                book_data = json.load(file)
                self.books = [Book.from_dict(item) for item in book_data]

        if self.members_file.exists():
            with open(self.members_file, "r") as file:
                member_data = json.load(file)
                self.members = [
                    Member.from_dict(item) for item in member_data
                ]

    def save_data(self):
        with open(self.books_file, "w") as file:
            json.dump(
                [book.to_dict() for book in self.books],
                file,
                indent=4
            )

        with open(self.members_file, "w") as file:
            json.dump(
                [member.to_dict() for member in self.members],
                file,
                indent=4
            )

    # ---------- ADD BOOK ----------

    def add_book(self):
        book_id = input("Enter Book ID: ").strip()

        if any(book.book_id == book_id for book in self.books):
            print("Book ID already exists!")
            return

        title = input("Enter Book Title: ").strip()
        author = input("Enter Author Name: ").strip()

        if not book_id or not title or not author:
            print("All fields are required!")
            return

        book = Book(book_id, title, author)
        self.books.append(book)

        self.save_data()
        print("Book added successfully!")

    # ---------- VIEW BOOKS ----------

    def view_books(self):
        if not self.books:
            print("No books available.")
            return

        for book in self.books:
            status = "Available" if book.is_available() else "Issued"

            print("\nBook ID:", book.book_id)
            print("Title:", book.title)
            print("Author:", book.author)
            print("Status:", status)

    # ---------- SEARCH BOOK ----------

    def search_book(self):
        book_id = input("Enter Book ID to search: ").strip()

        for book in self.books:
            if book.book_id == book_id:
                print("Book Found!")
                print("Title:", book.title)
                print("Author:", book.author)
                print(
                    "Status:",
                    "Available" if book.is_available() else "Issued"
                )
                return

        print("Book not found.")

    # ---------- REGISTER MEMBER ----------

    def register_member(self):
        member_id = input("Enter Member ID: ").strip()

        if any(member.member_id == member_id for member in self.members):
            print("Member ID already exists!")
            return

        name = input("Enter Member Name: ").strip()

        if not member_id or not name:
            print("All fields are required!")
            return

        member = Member(member_id, name)
        self.members.append(member)

        self.save_data()
        print("Member registered successfully!")

    # ---------- ISSUE BOOK ----------

    def issue_book(self):
        book_id = input("Enter Book ID: ").strip()
        member_id = input("Enter Member ID: ").strip()

        book = next(
            (b for b in self.books if b.book_id == book_id),
            None
        )

        member = next(
            (m for m in self.members if m.member_id == member_id),
            None
        )

        if book is None:
            print("Book not found!")
            return

        if member is None:
            print("Member not found!")
            return

        if not book.is_available():
            print("Book is already issued!")
            return

        book.issued_to = member_id
        member.borrow_book(book_id)

        self.save_data()
        print("Book issued successfully!")

    # ---------- RETURN BOOK ----------

    def return_book(self):
        book_id = input("Enter Book ID to return: ").strip()
        member_id = input("Enter Member ID: ").strip()

        book = next(
            (b for b in self.books if b.book_id == book_id),
            None
        )

        member = next(
            (m for m in self.members if m.member_id == member_id),
            None
        )

        if book is None or member is None:
            print("Book or member not found!")
            return

        if book.issued_to != member_id:
            print("This book is not issued to this member!")
            return

        book.issued_to = None
        member.return_book(book_id)

        self.save_data()
        print("Book returned successfully!")

    # ---------- VIEW ISSUED BOOKS ----------

    def view_issued_books(self):
        issued_books = [
            book for book in self.books
            if not book.is_available()
        ]

        if not issued_books:
            print("No books are currently issued.")
            return

        for book in issued_books:
            print("\nBook ID:", book.book_id)
            print("Title:", book.title)
            print("Issued to Member ID:", book.issued_to)

    # ---------- REMOVE BOOK ----------

    def remove_book(self):
        book_id = input("Enter Book ID to remove: ").strip()

        for book in self.books:
            if book.book_id == book_id:

                if not book.is_available():
                    print("Cannot remove an issued book!")
                    return

                self.books.remove(book)
                self.save_data()

                print("Book removed successfully!")
                return

        print("Book not found!")
