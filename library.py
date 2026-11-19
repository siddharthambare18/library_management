import sqlite3
con=sqlite3.connect("library.db")
cur=con.cursor()

cur.execute("PRAGMA foreign_keys=ON;")

cur.execute("""
        CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            is_available BOOLEAN
        ) 
"""
)
cur.execute("""
        CREATE TABLE IF NOT EXISTS members(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        ) 
"""
)

cur.execute("""
        CREATE TABLE IF NOT EXISTS transactions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER,
            member_id INTEGER,
            action TEXT,
            timestamp TEXT,
            FOREIGN KEY (book_id) REFERENCES books(id),
            FOREIGN KEY (member_id) REFERENCES members(id)
        ) 
"""
)
con.commit()
con.close()

class Book:
    def __init__(self, book_id, title, author, is_available):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.is_available=is_available

    def __str__(self):
        if self.is_available==1:
            status="Available"
        else:
            status="checkout"
        return f"[ID: {self.book_id}] '{self.title}' by {self.author} status: {status}"

class Member:
    def __init__(self, member_id, name):
        self.member_id=member_id
        self.name=name

    def __str__(self):
        return f"[Member id: {self.member_id}] Name: {self.name}"


class LibrarySystem:
    def __init__(self, db_name="library.db"):
        self.db_name=db_name

    def add_book(self, title,author,is_available):
        con=sqlite3.connect(self.db_name)
        cur=con.cursor()
        cur.execute("INSERT INTO books (title, author, is_available) VALUES (?, ?, 1)", (title, author))
        con.commit()
        con.close()
        print(f"success: '{title}' added to the library inventory")
    
    def register_member(self, name):
        con=sqlite3.connect(self.db_name)
        cur=con.cursor()
        cur.execute("INSERT INTO members (name) VALUES (?)", (name,))
        con.commit()
        con.close()
        print(f"success: '{name}' added to the library members")

    def display_books(self):
        con=sqlite3.connect(self.db_name)
        cur=con.cursor()
        cur.execute("SELECT id, title, author, is_available FROM books")
        rows=cur.fetchall()
        con.close()

        if not rows:
            print("The inventory is currently empty. ")
            return

        for row in rows:
            book_obj=Book(book_id=row[0], title=row[1], author=row[2], is_available=row[3])
            print(book_obj)
        print("-"*30)

    def borrow_book(self, member_id, book_id):
        con=sqlite3.connect(self.db_name)
        cur=con.cursor()
        cur.execute("SELECT title, is_available FROM books WHERE id=?",(book_id,))
        book=cur.fetchone()
        
        if not book:
            print(f"Error: book with id {book_id} does not exist.")
            con.close()
            return

        title=book[0]
        is_available=book[1]

        if not is_available:
            print("sorry book is already checked out")
            con.close()
            return

        cur.execute("UPDATE books SET is_available = 0 WHERE id=?",(book_id,))

        con.commit()
        con.close()
        print(f"success: book '{title}' has been borrowed!")

    def return_book(self,member_id, book_id):
        con=sqlite3.connect(self.db_name)
        cur=con.cursor()
        cur.execute("SELECT title, is_available FROM books WHERE id=?",(book_id,))
        book=cur.fetchone()

        if not book:
            print(f"Error: Book with ID {book_id} does not exist.")
            con.close()
            return
        title=book[0]
        is_available=book[1]
        if is_available==1:
            print(f"Error: '{title}' was not checked out.")
            con.close()
            return
        cur.execute("UPDATE books SET is_available=1 WHERE id=?", (book_id,))
        con.commit()
        con.close()
        print(f"Success: Book '{title}' has been returned!")


if __name__ =="__main__":
    lib=LibrarySystem()

    while True:
            print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
            print("1. Add a Book")
            print("2. Register a Member")
            print("3. View All Books")
            print("4. Borrow a Book")
            print("5. Return a Book")
            print("6. Exit")
            
            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                lib.add_book(title, author, 1)

            elif choice == "2":
                name = input("Enter member name: ")
                lib.register_member(name)

            elif choice == "3":
                lib.display_books()

            elif choice == "4":
                try:
                    member_id = int(input("Enter Member ID: "))
                    book_id = int(input("Enter Book ID to borrow: "))
                    lib.borrow_book(member_id, book_id)
                except ValueError:
                    print("Error: Please enter valid numbers for IDs.")

            elif choice == "5":
                try:
                    member_id = int(input("Enter Member ID: "))
                    book_id = int(input("Enter Book ID to return: "))
                    lib.return_book(member_id, book_id)
                except ValueError:
                    print("Error: Please enter valid numbers for IDs.")

            elif choice == "6":
                print("Exiting Library System. Goodbye! 👋")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 6.")