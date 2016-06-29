from datetime import datetime
from app import app, login_manager
from app.models.User import User
from app.forms.LoginForm import UserForm, InviteForm
from flask import render_template, flash, Response, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
import logging
import traceback


@app.route('/', methods=['GET', 'POST'])
def main():
    if current_user.is_anonymous:
        return redirect(url_for('login'))

    return render_template('main.html', user=current_user)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = UserForm(request.form, current_user)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.validate_password(form.password.data):
            login_user(user)
            user.update(last_login=datetime.now())

            return redirect('/')
        else:
            form.errors.update({'Authentication': ['Invalid username or password.', ]})

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login')


@app.route('/admin')
def admin():
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    if not current_user.is_admin:
        return redirect('/')

    return render_template('admin/admin.html', form=InviteForm(request.form, current_user))


@app.route('/invite', methods=['POST'], defaults={'invite_hash': None})
@app.route('/invite/<invite_hash>', methods=['GET'])
def invite(invite_hash):
    print(request.form)

    if invite_hash:
        from app.models.Invite import Invite
        invite = Invite.query.filter_by(invite=invite_hash).filter_by(activated=False).first()
        if not invite:
            user = User.query.filter_by(email=invite.email).first()
            invite.update(activated=True)
            login_user(user)
        return redirect('/login')

    else:
        user = User.init(request.form['email'], invite=invite_hash, active=True)
        # return redirect(url_for('/admin', messages={"main":'Invite message to {0} successfully send'.format(user.email)}))
        return redirect(url_for('admin'))


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.errorhandler(Exception)
def exception(e):
    if request.is_xhr or request.json:
        logging.error(traceback.format_exc())
        return Response(str(e), 500)

    flash(str(e))
    logging.error(traceback.format_exc())
    return redirect(request.args.get('next') or request.referrer or url_for('main'), code=303)
