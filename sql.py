import sqlite3

conn = sqlite3.connect("books.db")
c = conn.cursor()

# books = [
#     ("The Digging-est Dog", 72),
#     ("Goodnight Moon", 31),
#     ("The Giving Tree", 66)
# ]

# c.executemany("INSERT INTO books VALUES (?,?)", books)
# conn.commit()

c.execute("""CREATE TABLE if not exists books(
             title TEXT,
             pages INTEGER 
          )
""")

# c.execute("INSERT INTO books VALUES ('Are You My Mother?', 72)")
# conn.commit()

c.execute("UPDATE books SET pages=64 WHERE title = ?", ("The Giving Tree", ))
conn.commit()

c.execute("SELECT rowid, * FROM books WHERE title = ?", ("The Giving Tree",))
data = c.fetchone()
print(data)