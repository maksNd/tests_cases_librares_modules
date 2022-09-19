"""Наполнение БД"""

import sqlite3

with sqlite3.connect('books.sqlite') as connection:
    cursor = connection.cursor()

    query_insert_to_genres = """
            INSERT INTO genres (name)
            VALUES ('Horror'), ('Sci-Fi');
    """

    query_insert_to_author = """
            INSERT INTO author (name)
            VALUES ('Author 1'), ('Author 2'), ('Author 3');
    """

    query_insert_to_books = """
            INSERT INTO books (name, genre_id)
            VALUES ('Book 1', 1), ('Book 2', 2), ('Book 3', 2);
    """

    query_insert_to_book_author = """
            INSERT INTO book_author (book_id, author_id)
            VALUES (1, 1), (2, 1), (2, 3), (3, 2);
    """

    cursor.execute(query_insert_to_genres)
    cursor.execute(query_insert_to_author)
    cursor.execute(query_insert_to_books)
    cursor.execute(query_insert_to_book_author)

