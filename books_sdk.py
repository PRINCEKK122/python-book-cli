from books import Book
import sqlite3
import os.path

l = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

conn = sqlite3.connect(os.path.join(l, "books.db"))

c = conn.cursor()

book = Book("hello", 50)
print(book)