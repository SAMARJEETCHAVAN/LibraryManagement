class Book:
    """
    Represents a single book in the library.
    """

    def __init__(self, title, author, isbn):
        """
        Initialize a book with title, author, and ISBN.
        By default, a book is available for loan.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        self.borrowed_by = None  # Will store Member object when borrowed

    def __str__(self):
        """
        Return a readable string representation of the book.
        """
        status = 'Available' if self.available else f'Loaned to {self.borrowed_by.name}'
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"

    def mark_loaned(self, member):
        """
        Mark this book as loaned to a member.
        """
        self.available = False
        self.borrowed_by = member

    def mark_returned(self):
        """
        Mark this book as returned and available.
        """
        self.available = True
        self.borrowed_by = None
