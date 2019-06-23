# -*- coding: UTF-8 -*-

from flask import Blueprint, render_template, url_for,request,redirect, flash
from common.models.User import User
from flask_login import login_user, logout_user, login_required, current_user
from carsome import app,db
from flask_bootstrap import Bootstrap
from admin.forms import Login_Form, RegistrationForm

bootstrap=Bootstrap(app)

route_admin = Blueprint('admin', __name__, url_prefix='admin')

@route_admin.route('/')
@login_required
def index():
    return redirect(url_for('admin.login'))

@route_admin.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('admin/main.index'))

    form = Login_Form()
    if form.validate_on_submit():
            users = User.query.filter_by(email=form.email.data).first()
            if users is not None and users.verify_password(form.password.data):
                login_user(users, form.remember_me.data)
                next = request.args.get('next')
                if next is None or not next.startswith('/'):
                    next = url_for('admin/main.index')
                return redirect(next)
            flash(u'无效的凭证' )
    return render_template('admin/login.html', form=form)

@route_admin.route("/logout")
def logout():
	logout_user()
	flash('退出')
	return redirect(url_for('admin.login'))

@route_admin.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        # token = user.generate_confirmation_token()
        # send_email(user.email, 'Confirm Your Account',
        #            'auth/email/confirm', user=user, token=token)
        # flash('A confirmation email has been sent to you by email.')
        return redirect(url_for('admin.login'))
    return render_template('admin/register.html', form=form)

