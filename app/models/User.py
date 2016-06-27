from flask_user import UserMixin
from app import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.Unicode(255), nullable=False, server_default='', unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    active = db.Column(db.Boolean(), nullable=False, server_default='0')

    # User information
    first_name = db.Column(db.Unicode(50), nullable=False, server_default='')
    last_name = db.Column(db.Unicode(50), nullable=False, server_default='')

    invite = db.Column(db.Unicode(36), unique=True)

    is_admin = db.Column(db.Boolean(), nullable=False, server_default='0')

    def __repr__(self):
        return '{0}, {1} [admin:{2}]'.format(self.id, self.email, self.is_admin)

