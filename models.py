import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Publisher(Base):
    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=30), unique=True)

    book = relationship("Book", back_populates="publisher")

    def __str__(self):
        return f"Publisher: id = {self.id}, name = {self.name}"

class Book(Base):
    __tablename__ = "book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=50), unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)

    publisher = relationship("Publisher", back_populates="book")
    stock = relationship("Stock", back_populates="book")

    def __str__(self):
        return f"Book: id = {self.id}, title = {self.title}, id_publisher = {self.id_publisher}"

class Shop(Base):
    __tablename__ = "shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=20), unique=True)

    stock = relationship("Stock", back_populates="shop")

    def __str__(self):
        return f"Shop: id = {self.id}, name = {self.name}"

class Stock(Base):
    __tablename__ = "stock"

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    book = relationship("Book", back_populates="stock")
    shop = relationship("Shop", back_populates="stock")
    sale = relationship("Sale", back_populates="stock")

    def __str__(self):
        return f"Stock: id = {self.id}, id_book = {self.id_book}, id_shop = {self.id_shop}, count = {self.count}"

class Sale(Base):
    __tablename__ = "sale"

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.String(length=10), nullable=False)
    date_sale = sq.Column(sq.DateTime, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    stock = relationship("Stock", back_populates="sale")

    def __str__(self):
        return f"Sale: id = {self.id}, price = {self.price}, date_sale = {self.date_sale}, " \
               f"id_stock = {self.id_stock}, count = {self.count}."

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)