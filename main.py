import json

import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

from models import create_tables, Publisher, Shop, Book, Stock, Sale

DSN = 'postgresql://postgres:00000000@localhost:5432/bookhouse_db'
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

def get_shops():

# Store Search

    command = input("Enter a name or ID number: ")

    search_data = session.query(Shop).\
        join(Stock).\
        join(Book).\
        join(Publisher)
    if command.isdigit():
        _a = search_data.filter(Publisher.id == command).all()
    else:
        _a = search_data.filter(Publisher.name == command).all()
    for record in _a:

        print(record)

publisher1 = Publisher(id=1, name="O\u2019Reilly")
publisher2 = Publisher(id=2, name="Pearson")
publisher3 = Publisher(id=3, name="Microsoft Press")
publisher4 = Publisher(id=4, name="No starch press")

book1 = Book(id=1, title="Programming Python, 4th Edition", id_publisher=1)
book2 = Book(id=2, title="Learning Python, 4th Edition", id_publisher=1)
book3 = Book(id=3, title="Natural Language Processing with Python", id_publisher=1)
book4 = Book(id=4, title="Hacking: The Art of Exploitation", id_publisher=4)
book5 = Book(id=5, title="Modern Operating Systems", id_publisher=2)
book6 = Book(id=6, title="Code Complete: Second Edition", id_publisher=3)

shop1 = Shop(id=1, name="Labirint")
shop2 = Shop(id=2, name="OZON")
shop3 = Shop(id=3, name="Amazon")

stock1 = Stock(id=1, id_book=1, id_shop=1, count=34)
stock2 = Stock(id=2, id_book=2, id_shop=1, count=30)
stock3 = Stock(id=3, id_book=3, id_shop=1, count=0)
stock4 = Stock(id=4, id_book=5, id_shop=2, count=40)
stock5 = Stock(id=5, id_book=6, id_shop=2, count=50)
stock6 = Stock(id=6, id_book=4, id_shop=3, count=10)
stock7 = Stock(id=7, id_book=6, id_shop=3, count=10)
stock8 = Stock(id=8, id_book=1, id_shop=2, count=10)
stock9 = Stock(id=9, id_book=1, id_shop=3, count=10)

sale1 = Sale(id=1, price="50.05", date_sale="2018-10-25T09:45:24.552Z", count=16, id_stock=1)
sale2 = Sale(id=2, price="50.05", date_sale="2018-10-25T09:51:04.113Z", count=10, id_stock=3)
sale3 = Sale(id=3, price="10.50", date_sale="2018-10-25T09:52:22.194Z", count=9, id_stock=6)
sale4 = Sale(id=4, price="16.00", date_sale="2018-10-25T10:59:56.230Z", count=5, id_stock=5)
sale5 = Sale(id=5, price="16.00", date_sale="2018-10-25T10:59:56.230Z", count=5, id_stock=9)
sale6 = Sale(id=6, price="16.00", date_sale="2018-10-25T10:59:56.230Z", count=1, id_stock=4)

session.add_all([publisher1, publisher2, publisher3, publisher4])
session.add_all([book1, book2, book3, book4, book5, book6])
session.add_all([shop1, shop2, shop3])
session.add_all([stock1, stock2, stock3, stock4, stock5, stock6, stock7, stock8, stock9])
session.add_all([sale1, sale2, sale3, sale4, sale5, sale6])
session.commit()

if __name__ == '__main__':
    SELECT = get_shops()


session.close()