class Transaction:
    def __init__(self, transaction_id, book, member, issue_date, return_date=None):
        self.transaction_id = transaction_id
        self.book = book
        self.member = member
        self.issue_date = issue_date
        self.return_date = return_date

    def __str__(self):
        return f"Transaction ID: {self.transaction_id}, Book: {self.book.title}, Member: {self.member.name}, Issue Date: {self.issue_date}, Return Date: {self.return_date if self.return_date else 'Not Returned'}"
class Transaction:
    def __init__(self, transaction_id, book, member, issue_date, return_date=None):
        self.transaction_id = transaction_id
        self.book = book
        self.member = member
        self.issue_date = issue_date
        self.return_date = return_date

    def __str__(self):
        return f"Transaction ID: {self.transaction_id}, Book: {self.book.title}, Member: {self.member.name}, Issue Date: {self.issue_date}, Return Date: {self.return_date if self.return_date else 'Not Returned'}"
    