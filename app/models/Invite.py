from flask_user import UserMixin
from app import db
import datetime


class Invite(db.Model, UserMixin):
    __tablename__ = 'invites'

    invite = db.Column(db.Unicode(36), unique=True, nullable=False)
    email = db.Column(db.Unicode(30), unique=False, nullable=False)  # invite can be sent many times to one email
    created_at = db.Column(db.DateTime, default=datetime.now)
    activated = db.Column(db.BOOLEAN, default=False)

    def __repr__(self):
        return 'email: {0}, activated: {1}, invite: {2}'.format(self.email, self.activated, self.invite)

