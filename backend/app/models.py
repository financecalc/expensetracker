from app.extensions import db


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # The price will be saved in cents, no floats should be used because of rounding errors
    price = db.Column(db.Integer, index=True)
    name = db.Column(db.String(64))

    tags = db.relationship('Tag', secondary='transaction_tag', backref='transactions')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<Tag {}>'.format(self.name)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


transaction_to_tag = db.Table('transaction_to_tag',
                              db.Column('transaction_id', db.Integer, db.ForeignKey('transaction.id')),
                              db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                              )
