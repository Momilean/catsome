# -*- coding: UTF-8 -*-
from flask import Blueprint,render_template,url_for, send_from_directory
from carsome import app,db,  login_manager
from common.models.User import User
from flask_login import LoginManager, login_user, logout_user, login_required,  current_user
from flask.views import MethodView
route_admin_main = Blueprint('admin/main', __name__, url_prefix='admin')


#route_main = Blueprint('main', __name__, url_prefix='admin')
@route_admin_main.route('/avatars/<path:filename>')
def get_avater(filename):
	return send_from_directory( app.config['AVATARS_SAVE_PATH'], filename)

@login_manager.user_loader
def load_user (user_id):
	return User.query.get(int(user_id))

@route_admin_main.route("/index", methods=["GET","POST"])
@login_required
def index():
	f=load_user
	return render_template("admin/main/index.html" , f=f)