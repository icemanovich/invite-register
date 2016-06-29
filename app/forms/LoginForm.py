from app.models.User import User
from flask_wtf import LoginForm
from wtforms import StringField, validators
from wtforms.validators import DataRequired, Email, Length


class UserForm(LoginForm):
    email = StringField(label='Login', validators=[DataRequired(), Length(min=3), Email()])
    password = StringField(label='Password', validators=[DataRequired(), Length(min=3)])


class InviteForm(LoginForm):
    email = StringField(label='Login', validators=[DataRequired(), Length(min=3), Email()])

    def validate_invite(self):
        user = User.query.filter_by(email=self.email.data, active=False).first()
        if user:
            raise validators.ValidationError('User with email {0} already activated'.format(self.email.data))


class ConsoleRegisterForm(UserForm):

    def check_if_exists(self, field):
        user = User.query.filter_by(login=self.email.data).first()
        if user is not None:
            raise validators.ValidationError('User already exists.')

    def validate_csrf_token(self, field):
        pass

