# from config import load_config
# from flask import Flask
# from flask_mail import Mail
# from flask_migrate import Migrate, MigrateCommand
# from flask_user import UserManager, SQLAlchemyAdapter
# from flask_wtf.csrf import CsrfProtect
# import os
from app import app, db
from app.models.User import User
from datetime import datetime
# from app.models.Invite import Invite


def create_default_users():
    """ Create users when app starts """

    # Create all tables
    db.create_all()

    # Add users
    users = [
        ['admin@example.com', 'qwe'],
        ['master@example.com', 'qwe11']
    ]
    for user in users:
        find_or_create_user(user[0], user[1], True)

    # Save to DB
    db.session.commit()


def find_or_create_user(email, password, is_admin=False):
    """ Find existing user or create new user """
    user = User.query.filter(User.email == email).first()
    if not user:
        user = User.init(
            email=email,
            password=password,
            active=True,
            is_admin=is_admin
        )

        db.session.add(user)
    return user

