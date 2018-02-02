from models import Base, engine, session, Pizza, Option
from meals_catalog import meals


def insert_into_db(catalog):
    for meal in meals:
        pizza = Pizza(title=meal['title'], description=meal['description'])
        session.add(pizza)
        for choise in meal['choices']:
            option = Option(size=choise['title'], price=choise['price'])
            pizza.options.append(option)
        session.add(pizza)
    session.commit()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    insert_into_db(meals)
