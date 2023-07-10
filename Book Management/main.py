from member import Member
from book import Book
from loan import Loan

class LibraryManagement:
    def __init__(self):
        self.members = []
        self.books = []
        self.loans = []

    def display_menu(self):
        print("1. Add a new book")
        print("2. Add a new member")
        print("3. Issue a book")
        print("4. Return a book")
        print("5. Quit")

    def main(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.add_member()
            elif choice == "3":
                self.issue_book()
            elif choice == "4":
                self.return_book()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

    def add_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        book = Book(title, author)
        self.books.append(book)
        print("Book added successfully!")

    def add_member(self):
        name = input("Enter the name of the member: ")
        member_id = input("Enter the ID of the member: ")
        member = Member(name, member_id)
        self.members.append(member)
        print("Member added successfully!")

    def issue_book(self):
        book_title = input("Enter the title of the book: ")
        member_id = input("Enter the ID of the member: ")
        book = self.find_book(book_title)
        member = self.find_member(member_id)
        if book and member:
            loan = Loan(book, member)
            self.loans.append(loan)
            print("Book issued successfully!")
        else:
            print("Book or member not found. Please check the details.")

    def return_book(self):
        book_title = input("Enter the title of the book: ")
        member_id = input("Enter the ID of the member: ")
        loan = self.find_loan(book_title, member_id)
        if loan:
            self.loans.remove(loan)
            print("Book returned successfully!")
        else:
            print("Loan not found. Please check the details.")

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def find_loan(self, book_title, member_id):
        for loan in self.loans:
            if loan.book.title == book_title and loan.member.member_id == member_id:
                return loan
        return None

if __name__ == "__main__":
    library = LibraryManagement()
    library.main()