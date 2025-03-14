# 📚 Library Management System (Python + MySQL)

🚀 **A simple CLI-based Library Management System using Python and MySQL.**

---

## ✨ Features
- 📥 **Add a Book**
- 🗑️ **Remove a Book**
- 🔍 **Search Books (by Title/Author)**
- 📋 **Display All Books**
- 📊 **View Library Statistics**
- 🎯 **User-Friendly Interface**

---

## 🛠️ Setup Instructions

### 1️⃣ Install MySQL Connector
```bash
pip install mysql-connector-python
```

### 2️⃣ Create Database & Table
Run the following SQL queries in MySQL:
```sql
CREATE DATABASE LibraryDB;
USE LibraryDB;
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    year INT,
    genre VARCHAR(100),
    read_status BOOLEAN
);
```

### 3️⃣ Configure Database Connection
Modify your database connection details in the `connect_db()` function:
```python
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",  # Change to your MySQL password
        database="LibraryDB"
    )
```

---

## 📜 Usage Guide

### ➕ Add a Book
```python
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
```

### 🗑️ Remove a Book
```python
def remove_book():
    title = input("Enter the title of the book to remove: ")
    conn = connect_db()
    cursor = conn.cursor()
    query = "DELETE FROM books WHERE title = %s"
    cursor.execute(query, (title,))
    conn.commit()
    conn.close()
    print(f'🗑️ Book "{title}" removed successfully.')
```

### 🔍 Search Books
```python
def search_library():
    search_by = input("Search by (title/author): ").lower()
    search_term = input(f"Enter the {search_by}: ")
    conn = connect_db()
    cursor = conn.cursor()
    query = f"SELECT title, author, year, genre, read_status FROM books WHERE {search_by} LIKE %s"
    cursor.execute(query, (f"%{search_term}%",))
    results = cursor.fetchall()
    conn.close()
    for book in results:
        status = "read" if book[4] else "not read"
        print(f'📚 {book[0]} by {book[1]} ({book[2]}) - {status}')
```

### 📋 Display All Books
```python
def display_books():
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT title, author, year, genre, read_status FROM books"
    cursor.execute(query)
    books = cursor.fetchall()
    conn.close()
    for book in books:
        status = "read" if book[4] else "not read"
        print(f'📘 {book[0]} by {book[1]} ({book[2]}) - {status}')
```

### 📊 Library Statistics
```python
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
```

### 🎯 Main Menu
```python
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
```

### 🚀 Run the Program
```python
if __name__ == "__main__":
    main()
```

---

## 🤝 Contributing
Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).

---

## 💡 Author
👤 **Mohsin Raza**  
📧 mohsinraza2248gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/mohsin-raza-a514392b6)

---

🌟 **Don't forget to give this repo a star if you found it helpful!** ⭐

