from models import Base, engine, session, Pizza, Option
import json
import argparse
import os


def get_meals_catalog_path():
    parser = argparse.ArgumentParser()
    parser.add_argument('meals_catalog_path', help='Mandatory parametr')
    return parser.parse_args()


def load_meals_catalog_from_file(meals_catalog_path):
    if not os.path.exists(meals_catalog_path):
        return None
    with open(meals_catalog_path, 'r') as meals_catalog:
        return json.loads(meals_catalog.read())


def insert_into_db(meals):
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
    meals_catalog = get_meals_catalog_path()
    meals = load_meals_catalog_from_file(meals_catalog.meals_catalog_path)
    insert_into_db(meals)
