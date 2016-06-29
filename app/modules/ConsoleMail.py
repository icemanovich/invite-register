import smtplib
from flask import current_app
from app.models.Invite import Invite
from flask_mail import Mail, Message


class ConsoleMail(Mail):
    """ Modify default Flask mail driver to send messages in console

    """

    def send_invite(self, email: str):
        from app import app
        inv = Invite.init(email)
        msg = Message(
            "Welcome!",
            body='Check our page at {0}:{1}/invite/{2}'.format(app.config['APP_HOST'], app.config['APP_PORT'], inv.invite),
            sender="no-replay@example.com",
            recipients=[email, ]
        )

        return self.send(msg)

    def send_login(self, email: str, password: str):
        msg = Message(
            "Welcome!",
            body='Your invite has been accepted.\n login: {0}\n password: {1}'.format(email, password),
            sender=current_app.config['MAIL_FROM_EMAIL'],
            recipients=[email, ]
        )

        return self.send(msg)

    def send(self, message):
        """ Wrapper for message sender

        :param message:
        :return:
        """
        try:
            if not current_app.config['TESTING']:
                print('\n-------\n', message)
        except smtplib as e:
            current_app.logger.error(e)
            return False
        except Exception as e:
            current_app.logger.error(e)
            return False
        return True
