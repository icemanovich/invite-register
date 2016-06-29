from datetime import datetime
from flask_user import UserMixin
from app import db, mail
from app.models.ModelHelper import ModelHelper
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin, ModelHelper):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Unicode(255), nullable=False, server_default='', unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    active = db.Column(db.Boolean(), nullable=False, server_default='0')

    # Better to make reference to Invite table
    invite = db.Column(db.String(36), unique=True)

    is_admin = db.Column(db.Boolean(), nullable=False, server_default='0')

    created_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return "id: {0}, email: {1}, admin:{2}".format(self.id, self.email, self.is_admin)

    @staticmethod
    def init(email, password='', invite_hash=None, **kwargs):
        user = User.query.filter_by(email=email).first()
        if not user:
            user = User.create(
                email=email,
                password=generate_password_hash(password),
                created_at=datetime.now(),
                **kwargs
            )

            if invite_hash:
                user.update(invite=invite_hash)

        mail.send_invite(email)
        mail.send_login(email, password)
        return user

    def mark_admin(self, is_admin=True):
        self.update(is_admin=is_admin)
        self.save()

    def validate_password(self, password):
        return check_password_hash(self.password, password)
