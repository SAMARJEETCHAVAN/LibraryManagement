class Member:
    """
    Represents a library member who can borrow and reserve books.
    """

    def __init__(self, name, member_id):
        """
        Initialize a member with name and a unique member ID.
        """
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        self.reserved_books = []

    def borrow_book(self, book):
        """
        Add a book to the member's borrowed books list.
        """
        if book in self.borrowed_books:
            print(f"{self.name} has already borrowed this book.")
        else:
            self.borrowed_books.append(book)
            book.mark_loaned(self)

    def return_book(self, book):
        """
        Remove a book from the member's borrowed books list.
        """
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.mark_returned()
        else:
            print(f"{self.name} has not borrowed this book.")

    def reserve_book(self, book):
        """
        Add a book to the member's reserved books list.
        """
        if book in self.reserved_books:
            print(f"{self.name} has already reserved this book.")
        else:
            self.reserved_books.append(book)

    def __str__(self):
        """
        Return a readable string representation of the member.
        """
        return f"Member: {self.name} (ID: {self.member_id})"
