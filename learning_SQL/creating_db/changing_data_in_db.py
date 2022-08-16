"""
Добавление новых значений в бд (одиночное, множественное
"""
import sqlite3

with sqlite3.connect('books_db.sqlite') as connection:
    cursor = connection.cursor()

    """add_data_query - добавляет данные в бд"""
    add_data_query = """
            INSERT INTO books (name, pages_count)
            VALUES ('eth roadmap', 98854), ('Red book', 4467)
    """

    """update_data_query - обновит запись в бд"""
    update_data_query = """
            UPDATE books
            SET genre = 'Detective'
            WHERE id == 1
    """

    """update_data_query_2 - обновит запись в бд"""
    update_data_query_2 = """
            UPDATE books
            SET price = 100
            WHERE price is NULL
    """

    """update_data_query_3 - обновит запись в бд"""
    update_data_query_3 = """
            UPDATE books
            SET price = price + 30
            WHERE id IN (1, 2)
    """

    """delete_data_query - удалит запись из бд"""
    delete_data_query = """
            DELETE FROM books
            WHERE price < 130
    """

    cursor.execute(add_data_query)
