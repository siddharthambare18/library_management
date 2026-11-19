# 📚 SQLite3 Library Management System

A command-line Library Management System built in Python using Object-Oriented Programming (OOP) and `sqlite3` for persistent relational database storage. Designed to manage book inventory, member registrations, and check-out/return workflows cleanly from the terminal.

---

## ✨ Key Features

- **Book Inventory Management:** Add new books with titles, authors, and real-time availability tracking.
- **Member Registration:** Register library members with unique auto-incremented IDs.
- **Borrow & Return System:** Check out and return books with built-in validation to prevent double-borrowing or returning unborrowed items.
- **Relational Database Schema:** Uses SQLite3 with foreign key constraints (`books`, `members`, and `transactions` tables) for structured data persistence.
- **OOP Data Modeling:** Encapsulates database records into `Book` and `Member` classes with custom `__str__` formatting.
- **Input Error Handling:** Protects CLI workflows against non-numeric ID inputs using `try/except ValueError` blocks.

---

## 🛠️ Tech Stack & Concepts Used

- **Language:** Python 3.x
- **Database:** SQLite3 (`sqlite3` standard library)
- **Core Concepts:** Object-Oriented Programming (`Book`, `Member`, `LibrarySystem` classes), Relational SQL Schemas (`PRIMARY KEY`, `FOREIGN KEY`), Parameterized SQL Queries (preventing SQL injection), and Exception Handling (`try/except`).

---

## 🗄️ Database Schema

The application automatically initializes `library.db` with three tables on startup:
- **`books`**: `id` (PK), `title`, `author`, `is_available`
- **`members`**: `id` (PK), `name`
- **`transactions`**: `id` (PK), `book_id` (FK), `member_id` (FK), `action`, `timestamp`

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone [https://github.com/siddharthambare18/library-management-system.git](https://github.com/siddharthambare18/library-management-system.git)
cd library-management-system
