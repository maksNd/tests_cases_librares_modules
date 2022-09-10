from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from declarative_method import Book, Author, Genre
from declarative_method import create_db

# подключаемся к бд
engine = create_engine('sqlite:///authors_books.db')

create_db()

session = sessionmaker(bind=engine)
s = session()

author_1 = Author(name='Lutz')
author_2 = Author(name='Mutz')
author_3 = Author(name='Shmutz')

genre_1 = Genre(name='detective')
genre_2 = Genre(name='programming')
genre_3 = Genre(name='learning')
genre_4 = Genre(name='fun')

book_1 = Book(title='питон1', genre=genre_1, author=author_1, price=500)
book_2 = Book(title='чистый питон', genre=genre_2, author=author_2, price=500)
book_3 = Book(title='питон33', genre=genre_3, author=author_3, price=500)
book_4 = Book(title='Чистый чистый питон4', genre=genre_4, author=author_1, price=500)
book_5 = Book(title='Чистый5', genre=genre_1, author=author_2, price=500)
book_6 = Book(title='Чистый56', genre=genre_2, author=author_3, price=500)

book_7 = Book(title='питон1', genre=genre_1, price=500)
author_4 = Author(name='Kutz', book=book_7)

s.add_all([book_1, book_2, book_3, book_4, book_5, book_6])
s.add(author_4)
s.commit()
