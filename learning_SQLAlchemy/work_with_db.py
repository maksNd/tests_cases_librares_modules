from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from declarative_method import Base, Book, Author, Genre
from declarative_method import create_db

# подключаемся к бд
engine = create_engine('sqlite:///authors_books.db')

create_db()

session = sessionmaker(bind=engine)
s = session()

author_1 = Author(name='Lutz')
author_2 = Author(name='Mutz')

# genre_1 = Genre(genre_name='programming')
# genre_2 = Genre(genre_name='learning')
# genre_3 = Genre(genre_name='fun')

book_5 = Book(title='Чистый чистый питон', genre='programming', price=500)
"""Можно добавить автора с книгами (книги добавятся автоматически в свою таблицу книг)"""
author_3 = Author(name='Smutz', book=[book_5])

"""Можно добавить книгу с автором (автор добавится автоматически в свою таблицу авторов)"""
book_1 = Book(title='Чистый чистый питон', author=author_1, price=500)
book_2 = Book(title='Чистый чистый питон1', author=author_2, price=500)
book_3 = Book(title='Чистый чистый питон2', author=author_1, price=500)
book_4 = Book(title='Чистый чистый питон3', author=author_2, price=500)
book_44 = Book(title='питон44', author_id=2, genre='programming', price=500)

s.add_all([book_1, book_2, book_3, book_4, book_44])
s.add(author_3)

s.commit()
