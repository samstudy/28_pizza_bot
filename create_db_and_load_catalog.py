from models import Base, engine, session, Pizza, Option
from catalog import catalog


def insert_into_db(catalog):
    for meal in catalog:
        pizza = Pizza(title=meal['title'], description=meal['description'])
        session.add(pizza)
        for choise in meal['choices']:
            option = Option(size=choise['title'], price=choise['price'])
            pizza.options.append(option)
        session.add(pizza)
    session.commit()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    insert_into_db(catalog)
