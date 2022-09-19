import sqlite3

with sqlite3.connect('books.sqlite') as connection:
    cursor = connection.cursor()

    # INNER JOIN обязывает все результаты вернуться в ответе
    # LEFT JOIN не обязывает все результаты вернуться в ответе
    query_1 = """
        SELECT *
        FROM books
        INNER JOIN genres on books.genre_id = genres.id
        """

    query_2 = """
        SELECT books.name as 'book_name', genres.name as 'genre_name' 
        FROM books
        INNER JOIN genres on books.genre_id = genres.id 
        """

    query_3 = """
        SELECT 
            books.name as 'book_name',
            genres.name as 'genre_name',
            book_author.*
        FROM books
        INNER JOIN genres on books.genre_id = genres.id
        LEFT JOIN book_author on books.id = book_author.book_id
        """

    query_4 = """
        SELECT 
            books.name as 'book_name',
            genres.name as 'genre_name',
            author.name as author_name
        FROM books
        INNER JOIN genres on books.genre_id = genres.id
        LEFT JOIN book_author on books.id = book_author.book_id
        LEFT JOIN author on book_author.author_id = author.id 
        """

    cursor.execute(query_4)
    for i in cursor.fetchall():
        print(i)