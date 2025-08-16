"""
Library Transactions
"""

class Loans:

    def __init__(self, user_id, book_id, library_id, borrowed_at, due_date, returned_at, status):
        self.user_id = user_id
        self.book_id = book_id
        self.library_id = library_id
        self.borrowed_at = borrowed_at
        self.due_date = due_date
        self.returned_at = returned_at
        self.status = status

    def check_out(self):
        pass

    def check_in(self):
        pass


class Fines(Loans):
    
    def __init__(self, user_id, loan_id, amount, paid, issued_at, paid_at):
        super().__init__(user_id, loan_id)
        self.amount = amount
        self.paid = paid
        self.issued_at = issued_at
        self.paid = paid_at

    def issue_fine(self):
        pass


    def pay(self):
        pass

    