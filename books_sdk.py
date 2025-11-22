import sqlite3
from os import getcwd
from os.path import dirname, join, realpath

from books import Book

db_path = join(realpath(join(getcwd(), dirname(__file__))), "books.db")


def setup_db():
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        c.execute(
            """CREATE TABLE IF NOT EXISTS books(
                title TEXT,
                pages INTEGER
            )"""
        )


setup_db()
# conn = sqlite3.connect(os.path.join(l, "books.db"))

# c = conn.cursor()


def add_book(book):
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO books VALUES (?, ?)", (book._title, book._pages))
        return c.lastrowid


def get_books():
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        result = c.execute("SELECT * FROM books").fetchall()
        return [Book(book[0], book[1]) for book in result]


def get_book_by_title(title):
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        result = c.execute("SELECT * FROM books WHERE title = ?", (title,)).fetchone()

        if result:
            return Book(result[0], result[1])
        return None
    
def delete_book_by_title(title):
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        result = c.execute("DELETE FROM books WHERE title = ?", (title,))
        return c.rowcount
    
def delete_book(book):
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        result = c.execute("DELETE FROM books WHERE title = ?", (book.title, ))
        return c.rowcount


# data = get_books()
# data = get_book_by_title("This is a test book")
# print(data)
# add_book(Book("This is a test book", 69))
# print(delete_book_by_title("This is a test book"))
