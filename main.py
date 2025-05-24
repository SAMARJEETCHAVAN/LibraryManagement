from library import Library
from book import Book
from member import Member


def main():
    """
    Entry point for the Library Management System.
    """
    library = Library()

    # Prepopulate some books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "12345")
    book2 = Book("1984", "George Orwell", "67890")
    book3 = Book("To Kill a Mockingbird", "Harper Lee", "54321")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Prepopulate some members
    member1 = Member("Samarjeet", "M001")
    member2 = Member("Aditi", "M002")
    member3 = Member("Surya", "M003")
    library.register_member(member1)
    library.register_member(member2)
    library.register_member(member3)

    # Menu interaction loop
    while True:
        print("\nLibrary Management System")
        print("1. Add a New Book")
        print("2. Register a New Member")
        print("3. Loan a Book")
        print("4. Return a Book")
        print("5. Search Books")
        print("6. Visit User Profile")
        print("7. List Borrowed Books")
        print("8. Reserve a Book")
        print("9. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            isbn = input("Enter book ISBN: ").strip()
            new_book = Book(title, author, isbn)
            library.add_book(new_book)

        elif choice == '2':
            name = input("Enter member name: ").strip()
            member_id = input("Enter member ID: ").strip()
            new_member = Member(name, member_id)
            library.register_member(new_member)

        elif choice == '3':
            member_id = input("Enter member ID: ").strip()
            isbn = input("Enter book ISBN: ").strip()
            library.loan_book(member_id, isbn)

        elif choice == '4':
            member_id = input("Enter member ID: ").strip()
            isbn = input("Enter book ISBN: ").strip()
            library.return_book(member_id, isbn)

        elif choice == '5':
            keyword = input("Enter search keyword (title or author): ").strip()
            results = library.search_books(keyword)
            if results:
                print("Search Results:")
                for book in results:
                    print(f"- {book}")
            else:
                print("No books found.")

        elif choice == '6':
            member_id = input("Enter member ID to view profile: ").strip()
            member = library.members.get(member_id)
            if member:
                print(f"\nProfile for {member.name} (ID: {member.member_id})")
                print("Borrowed Books:")
                if member.borrowed_books:
                    for book in member.borrowed_books:
                        print(f"- {book.title}")
                else:
                    print("No borrowed books.")

                print("Reserved Books:")
                if member.reserved_books:
                    for book in member.reserved_books:
                        print(f"- {book.title}")
                else:
                    print("No reserved books.")
            else:
                print("Member not found.")

        elif choice == '7':
            library.list_borrowed_books()

        elif choice == '8':
            member_id = input("Enter member ID: ").strip()
            isbn = input("Enter book ISBN: ").strip()
            library.reserve_book(member_id, isbn)

        elif choice == '9':
            print("Exiting Library System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
