import datetime

#  Book Class 
class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = 'Available'  # By default, the book is available

    def __str__(self):
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Year: {self.year}, Status: {self.status}"

#  Member Class 
class Member:
    def __init__(self, member_id, name, phone):
        self.member_id = member_id
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"Member ID: {self.member_id}, Name: {self.name}, Phone: {self.phone}"

#  Transaction Class 
class Transaction:
    def __init__(self, transaction_id, book, member, issue_date, return_date=None):
        self.transaction_id = transaction_id
        self.book = book
        self.member = member
        self.issue_date = issue_date
        self.return_date = return_date

    def __str__(self):
        return f"Transaction ID: {self.transaction_id}, Book: {self.book.title}, Member: {self.member.name}, Issue Date: {self.issue_date}, Return Date: {self.return_date if self.return_date else 'Not Returned'}"

#  Library Class 
class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = []

    #  Add Book
    def add_book(self, title, author, year):
        book_id = len(self.books) + 1
        new_book = Book(book_id, title, author, year)
        self.books.append(new_book)
        print(f"Book '{title}' added successfully!")

    #   Add Member
    def add_member(self, name, phone):
        member_id = len(self.members) + 1
        new_member = Member(member_id, name, phone)
        self.members.append(new_member)
        print(f"Member '{name}' added successfully!")

    #  Issue Book
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

    #   Return Book
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

    #   View All Books
    def view_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    #   View All Members
    def view_members(self):
        if not self.members:
            print("No members in the library.")
        else:
            for member in self.members:
                print(member)

    #  View All Transactions (Issues & Returns)
    def view_transactions(self):
        if not self.transactions:
            print("No transactions in the library.")
        else:
            for transaction in self.transactions:
                print(transaction)

    #   Helper Method: Get Book by ID
    def get_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    #  Helper Method: Get Member by ID
    def get_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

#  Main Program (CLI)
def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. View All Books")
        print("6. View All Members")
        print("7. View All Transactions")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = int(input("Enter year of publication: "))
            library.add_book(title, author, year)

        elif choice == '2':
            name = input("Enter member name: ")
            phone = input("Enter member phone: ")
            library.add_member(name, phone)

        elif choice == '3':
            book_id = int(input("Enter book ID to issue: "))
            member_id = int(input("Enter member ID to issue book to: "))
            library.issue_book(book_id, member_id)

        elif choice == '4':
            book_id = int(input("Enter book ID to return: "))
            library.return_book(book_id)

        elif choice == '5':
            library.view_books()

        elif choice == '6':
            library.view_members()

        elif choice == '7':
            library.view_transactions()

        elif choice == '8':
            print("Exiting the Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

#   Running the program
if __name__ == "__main__":
    main()
