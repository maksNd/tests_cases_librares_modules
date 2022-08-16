"""
Таблица - books
Столбцы - name, author, description, genre, publication_date, page_count, price

ADD, RENAME, DROP
"""

import sqlite3

with sqlite3.connect('books_db.sqlite') as connection:
    cursor = connection.cursor()

    """rename_query - переименует название столбца"""
    rename_query = """
            ALTER TABLE books
            RENAME description TO text
    """

    """add_query - добавит колонку"""
    add_query = """
            ALTER TABLE books
            ADD country varchar(80)
    """

    """drop_query - удалит столбец 
    !!!не сработает в sqlite (т.к. sqlite не поддерживает динамическое изменение колонок)"""
    drop_query = """
            ALTER TABLE books
            DROP COLUMN country
    """

    """drop_table_query - удалит всю таблицу (структуру и данные)"""
    drop_table_query = """
            DROP books_2;
            DROP books_3;
    """
    cursor.executescript(drop_table_query)  # для удаления сразу 2х таблиц используется executescript()

    cursor.execute(add_query)
