"""
Smart Library System – Python Practice Task

Q1. Create two dictionaries:
    - library_members: to store all members and their borrowed books.
    - book_catalog: to store available books in the library.

Q2. create_member() Function:
    - Ask the user to enter a unique member_id.
    - Check if the member already exists.
    - If not, ask for the member's full name.
    - Add the new member to the library_members dictionary with an empty list of borrowed books.

Q3. insert_book() Function:
    - Ask for a unique book ID and book title.
    - Check whether the book ID already exists in the book_catalog.
    - If not, add the book to the catalog.

Q4. borrow_book() Function:
    - Ask for the member_id.
    - Check if the member exists.
    - If yes, check how many books they have borrowed (maximum = 3).
    - Display available books from book_catalog.
    - Ask for the book ID to borrow and add that book to the member's list.

Q5. delete_member() Function:
    - Ask for the member_id.
    - If the member exists, remove them from the library_members dictionary.

Q6. view_member_info() Function:
    - Ask for the member_id.
    - If the member exists, display their name and list of borrowed books.

Q7. view_all_members() Function:
    - Check if there are any members in the dictionary.
    - Loop through all members and print their ID, name, and borrowed books.

Q8. 
    - Display a menu with the following options:
        1. Create Member
        2. Insert Book
        3. Borrow Book
        4. Delete Member
        5. View Member Info
        6. View All Members
        7. Exit
    - Ask the user to enter a choice and call the correct function.
    - Loop until the user chooses to Exit.
"""


library_members = {}
book_catalog = {}

def create_member():
    member_id = input("Enter member ID: ")
    if member_id in library_members:
        print("Member already exists.")
    else:
        name = input("Enter member name: ")
        library_members[member_id] = {'name': name, 'borrowed_books': []}
        print(f"Member {name} created successfully.")

def insert_book():
    book_id = input("Enter book ID: ")
    if book_id in book_catalog:
        print("Book already exists in catalog.")
    else:
        title = input("Enter book title: ")
        book_catalog[book_id] = title
        print(f"Book '{title}' inserted into catalog.")

def borrow_book():
    member_id = input("Enter member ID: ")
    if member_id not in library_members:
        print("Member not found.")
        return

    if len(library_members[member_id]['borrowed_books']) >= 3:
        print("This member has already borrowed 3 books.")
        return

    print("Available Books:")
    for book_id, title in book_catalog.items():
        print(f"{book_id} - {title}")

    book_id = input("Enter book ID to borrow: ")
    if book_id in book_catalog:
        title = book_catalog.pop(book_id)
        library_members[member_id]['borrowed_books'].append(title)
        print(f"Book '{title}' borrowed by {library_members[member_id]['name']}.")
    else:
        print("Book not available or already borrowed.")

def delete_member():
    member_id = input("Enter member ID: ")
    if member_id in library_members:
        del library_members[member_id]
        print("Member deleted successfully.")
    else:
        print("Member not found.")

def view_member_info():
    member_id = input("Enter member ID: ")
    if member_id in library_members:
        print(f"Member Name: {library_members[member_id]['name']}")
        print(f"Borrowed Books: {library_members[member_id]['borrowed_books']}")
    else:
        print("Member not found.")

def view_all_members():
    if not library_members:
        print("No members found.")
    else:
        for member_id, info in library_members.items():
            print(f"ID: {member_id}")
            print(f"Name: {info['name']}")
            print(f"Borrowed Books: {info['borrowed_books']}")


while True:
        print("===== Library System Menu =====")
        print("1. Create Member")
        print("2. Insert Book")
        print("3. Borrow Book")
        print("4. Delete Member")
        print("5. View Member Info")
        print("6. View All Members")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            create_member()
        elif choice == "2":
            insert_book()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            delete_member()
        elif choice == "5":
            view_member_info()
        elif choice == "6":
            view_all_members()
        elif choice == "7":
            print("Exiting system.")
            break
        else:
            print("Invalid choice.")
