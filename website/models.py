from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    created_date = db.Column(db.Date(), default=func.now())
    shopping_list = db.relationship('Notes')

class Notes(db.Model):

    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(50))
    created_date = db.Column(db.Date(), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
