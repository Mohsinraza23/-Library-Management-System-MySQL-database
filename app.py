import mysql.connector

# ✅ Database Connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="mohsinraza",  # 👈 Yahan apna MySQL password likho
        database="LibraryDB"
    )

# ✅ Add a Book to MySQL
def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = input("Enter the year of the book: ")
    genre = input("Enter the genre of the book: ")
    read_status = input("Have you read the book? (yes/no): ").lower() == "yes"

    conn = connect_db()
    cursor = conn.cursor()
    
    query = "INSERT INTO books (title, author, year, genre, read_status) VALUES (%s, %s, %s, %s, %s)"
    values = (title, author, year, genre, read_status)
    
    cursor.execute(query, values)
    conn.commit()
    conn.close()

    print(f'✅ Book "{title}" added successfully.')

# ✅ Remove a Book
def remove_book():
    title = input("Enter the title of the book to remove: ")

    conn = connect_db()
    cursor = conn.cursor()

    query = "DELETE FROM books WHERE title = %s"
    cursor.execute(query, (title,))
    conn.commit()

    if cursor.rowcount > 0:
        print(f'🗑️ Book "{title}" removed successfully.')
    else:
        print(f'❌ Book "{title}" not found.')

    conn.close()

# ✅ Search Books
def search_library():
    search_by = input("Search by (title/author): ").lower()
    if search_by not in ["title", "author"]:
        print("❌ Invalid search type. Use 'title' or 'author'.")
        return

    search_term = input(f"Enter the {search_by}: ")

    conn = connect_db()
    cursor = conn.cursor()

    query = f"SELECT title, author, year, genre, read_status FROM books WHERE {search_by} LIKE %s"
    cursor.execute(query, (f"%{search_term}%",))
    results = cursor.fetchall()

    conn.close()

    if results:
        for book in results:
            status = "read" if book[4] else "not read"
            print(f'📚 {book[0]} by {book[1]} ({book[2]}) - {status}')
    else:
        print(f'❌ No books found matching "{search_term}".')

# ✅ Display All Books
def display_books():
    conn = connect_db()
    cursor = conn.cursor()
    
    query = "SELECT title, author, year, genre, read_status FROM books"
    cursor.execute(query)
    books = cursor.fetchall()
    
    conn.close()

    if not books:
        print("📭 The library is empty.")
        return

    print("\n📖 Library Collection:")
    for book in books:
        status = "read" if book[4] else "not read"
        print(f'📘 {book[0]} by {book[1]} ({book[2]}) - {status}')

# ✅ Display Statistics
def display_statistics():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM books")
    total_books = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM books WHERE read_status = TRUE")
    read_books = cursor.fetchone()[0]

    conn.close()

    perc_read = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f'📊 Total books: {total_books}')
    print(f'📖 Books read: {read_books}')
    print(f'📈 Percentage read: {perc_read:.2f}%')

# ✅ Main Function
def main():
    while True:
        print("\n📚 Library Menu:")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search Books")
        print("4. Display All Books")
        print("5. Display Statistics")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_library()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# ✅ Run the Program
if __name__ == "__main__":
    main()
