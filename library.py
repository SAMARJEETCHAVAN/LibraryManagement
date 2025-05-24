from book import Book
from member import Member


class Library:
    """
    Represents the library system.
    Manages books, members, loans, returns, and reservations.
    """

    def __init__(self):
        """
        Initialize an empty library.
        """
        self.books = {}  # ISBN -> Book
        self.members = {}  # Member ID -> Member

    def add_book(self, book):
        """
        Add a book to the library collection.
        """
        if book.isbn in self.books:
            print(f"Book with ISBN {book.isbn} already exists.")
        else:
            self.books[book.isbn] = book
            print(f"Book '{book.title}' added to the library.")

    def register_member(self, member):
        """
        Register a new library member.
        """
        if member.member_id in self.members:
            print(f"Member with ID {member.member_id} already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Member '{member.name}' registered.")

    def loan_book(self, member_id, isbn):
        """
        Loan a book to a member if available.
        """
        member = self.members.get(member_id)
        book = self.books.get(isbn)

        if not member:
            print(f"Member with ID {member_id} not found.")
            return

        if not book:
            print(f"Book with ISBN {isbn} not found.")
            return

        if not book.available:
            print(f"Book '{book.title}' is currently loaned out.")
            return

        member.borrow_book(book)
        print(f"Book '{book.title}' loaned to {member.name}.")

    def return_book(self, member_id, isbn):
        """
        Return a book from a member.
        """
        member = self.members.get(member_id)
        book = self.books.get(isbn)

        if not member:
            print(f"Member with ID {member_id} not found.")
            return

        if not book:
            print(f"Book with ISBN {isbn} not found.")
            return

        member.return_book(book)
        print(f"Book '{book.title}' returned by {member.name}.")

    def search_books(self, keyword):
        """
        Search for books by title or author.
        """
        results = []
        for book in self.books.values():
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                results.append(book)
        return results

    def list_borrowed_books(self):
        """
        List all borrowed books.
        """
        print("Borrowed Books:")
        for book in self.books.values():
            if not book.available:
                print(f"- {book}")

    def reserve_book(self, member_id, isbn):
        """
        Allow a member to reserve a book.
        """
        member = self.members.get(member_id)
        book = self.books.get(isbn)

        if not member:
            print(f"Member with ID {member_id} not found.")
            return

        if not book:
            print(f"Book with ISBN {isbn} not found.")
            return

        member.reserve_book(book)
        print(f"Book '{book.title}' reserved by {member.name}.")
