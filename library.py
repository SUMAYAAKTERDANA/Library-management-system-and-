import book
from library  import Book
from library  import Member
from library  import Transaction
import datetime

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = []

    def add_book(self, title, author, year):
        book_id = len(self.books) + 1
        new_book = Book(book_id, title, author, year)
        self.books.append(new_book)
        print(f"Book '{title}' added successfully!")

    def add_member(self, name, phone):
        member_id = len(self.members) + 1
        new_member = Member(member_id, name, phone)
        self.members.append(new_member)
        print(f"Member '{name}' added successfully!")

    def issue_book(self, book_id, member_id):
        book = self.get_book_by_id(book_id)
        member = self.get_member_by_id(member_id)

        if book and member and book.status == 'Available':
            issue_date = datetime.datetime.now().strftime("%Y-%m-%d")
            transaction_id = len(self.transactions) + 1
            transaction = Transaction(transaction_id, book, member, issue_date)
            self.transactions.append(transaction)
            book.status = 'Not Available'
            print(f"Book '{book.title}' issued to member '{member.name}' on {issue_date}.")
        else:
            print("Either the book is unavailable or the member does not exist.")

    def return_book(self, book_id):
        book = self.get_book_by_id(book_id)
        if book:
            for transaction in self.transactions:
                if transaction.book.book_id == book_id and transaction.return_date is None:
                    return_date = datetime.datetime.now().strftime("%Y-%m-%d")
                    transaction.return_date = return_date
                    book.status = 'Available'
                    print(f"Book '{book.title}' returned on {return_date}.")
                    return
            print("This book was not issued.")
        else:
            print("Book not found.")

    def view_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    def view_members(self):
        if not self.members:
            print("No members in the library.")
        else:
            for member in self.members:
                print(member)

    def view_transactions(self):
        if not self.transactions:
            print("No transactions in the library.")
        else:
            for transaction in self.transactions:
                print(transaction)

    def get_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def get_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
    