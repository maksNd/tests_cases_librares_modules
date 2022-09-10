"""
https://www.youtube.com/watch?v=sIbzKA6MId8&t=1300s

Декларативный вариант работы с БД
"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

"""
echo=True - продублирует комманды в виде SQL
"""
engine = create_engine('sqlite:///authors_books.db', echo=True)
Base = declarative_base()  #

# создаем таблицы
"""Т.к мы наследуемся от declarative_base(), то и класс и таблица создаются и связываются одновременно"""


class Book(Base):
    __tablename__ = 'book'

    id_book = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    author_id = Column(Integer, ForeignKey('author.id_author'))
    genre_id = Column(Integer, ForeignKey('genre.id_genre'))
    price = Column(Integer, nullable=False)
    author = relationship('Author', foreign_keys=[author_id])  # т.о мы указываем связь с другой таблицей
    genre = relationship('Genre')  # т.о мы указываем связь с другой таблицей


class Author(Base):
    __tablename__ = 'author'

    id_author = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    book_id = Column(Integer, ForeignKey('book.id_book'))
    book = relationship('Book', foreign_keys=[book_id])  # связь 1 ко многим


class Genre(Base):
    __tablename__ = 'genre'

    id_genre = Column(Integer, primary_key=True)
    name = Column(String(100))
    book = relationship('Book')  # связь 1 ко многим?


def create_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


create_db()
