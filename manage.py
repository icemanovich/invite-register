from app import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.models.User import User
from app.forms.LoginForm import ConsoleRegisterForm


migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def invite_user(email, password):
    """
    Creates new user (login=<email>) or updates its password
    """

    form = ConsoleRegisterForm(email=email, password=password)
    if form.validate():
        try:
            User.init(email, password, None, is_admin=True)
            print('Admin-user created (%s)') % email
        except Exception as e:
            print(e)
    else:
        print(form.errors)


@manager.command
def create_default_users():
    """
    Creates new default users
    """

    # Create all tables
    db.create_all()

    users = [
        ['admin@example.com', 'qwe'],
        ['master@example.com', 'qwe']
    ]
    for item in users:
        email = item[0]
        password = item[1]
        user = User.query.filter(User.email == email).first()
        if not user:
            user = User.init(email=email, password=password, active=True, is_admin=True)
            db.session.add(user)

    # Save to DB
    db.session.commit()


#
# @manager.command
# def test():
#     """Run the unit tests."""
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)
#     if COV:
#         COV.stop()
#         COV.save()
#         print('Coverage Summary:')
#         COV.report()
#         basedir = os.path.abspath(os.path.dirname(__file__))
#         covdir = os.path.join(basedir, 'tmp/coverage')
#         COV.html_report(directory=covdir)
#         print('HTML version: file://%s/index.html' % covdir)
#         COV.erase()
#

if __name__ == '__main__':
    manager.run()
