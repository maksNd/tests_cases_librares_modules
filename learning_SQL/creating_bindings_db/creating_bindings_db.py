"""Создание связанных таблиц"""
"""
FOREIGN KEY - внешний ключ для для связи таблиц
REFERENCES - указание ссылки для внешнего ключа
"""

import sqlite3

with sqlite3.connect('books.sqlite') as connection:
    cursor = connection.cursor()

    query_create_table_genres = """
            CREATE TABLE genres (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(100) NOT NULL   
                )
            """

    # FOREIGN KEY - внешний ключ для связи таблиц
    # REFERENCES - указание ссылки для внешнего ключа
    query_create_table_books = """
            CREATE TABLE books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(100) NOT NULL,
                genre_id INTEGER,
                FOREIGN KEY(genre_id) REFERENCES genres(id) ON DELETE SET NULL ON UPDATE CASCADE
                )
            """
    query_create_table_author = """
            CREATE TABLE author (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(100) NOT NULL
                )
            """

    # В это случае ПЕРВИЧНЫЙ КЛЮЧ представляет собой совокупность значений двух колонок
    query_create_table_book_author = """
            CREATE TABLE book_author (
                book_id INTEGER,
                author_id INTEGER,
                PRIMARY KEY (book_id, author_id),
                FOREIGN KEY (book_id) REFERENCES books(id),
                FOREIGN KEY (author_id) REFERENCES author(id)
                )
            """

    cursor.execute(query_create_table_genres)
    cursor.execute(query_create_table_books)
    cursor.execute(query_create_table_author)
    cursor.execute(query_create_table_book_author)
