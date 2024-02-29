import csv

from sqlalchemy.exc import NoResultFound

from app.extensions import db
from app.models import Transaction, Tag

'''
The CSV format should contain:
date,price,name
'''


def import_json(csv_string):
    rows = csv.reader(csv_string, delimiter=',')

    column_date = -1
    column_price = -1
    column_name = -1

    for index, element in enumerate(next(rows)):
        if element == 'date':
            column_date = index
        elif element == 'price':
            column_price = index
        elif element == 'name':
            column_name = index

    if column_date == -1 or column_price == -1 or column_name == -1:
        raise Exception('Missing at least one column')

    for row in rows:
        transaction = Transaction(price=int(row[column_price]), name=row[column_name])
        tags = get_tags(row[column_name])
        transaction.tags.append(tags)
        db.session.add(transaction)

    db.session.commit()


# TODO: Add other filter criteria like price
def get_tags(name):
    return [fetch_or_create_tag('A'), fetch_or_create_tag('B')]


def fetch_or_create_tag(name):
    try:
        return Tag.query.filter_by(name=name).first()
    except NoResultFound as e:
        tag = Tag(name=name)
        db.session.add(tag)
        db.session.commit()
        return tag
