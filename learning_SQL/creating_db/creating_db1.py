import sqlite3

with sqlite3.connect('books_db.sqlite') as connection:
    cursor = connection.cursor()

    query_1 = """
        CREATE TABLE book (
            id integer PRIMARY KEY AUTOINCREMENT,
            name text
        )"""
    query_2 = """
        CREATE TABLE genre (
            id integer PRIMARY KEY AUTOINCREMENT,
            name text
        )"""
    query_3 = """
        CREATE TABLE book_genre (
            book_id integer,
            genre_id integer
        )
    """

    cursor.execute(query_1)
    cursor.execute(query_2)
    cursor.execute(query_3)
