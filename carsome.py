# -*- coding: UTF-8 -*-
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_avatars import Avatars
import os


db = SQLAlchemy()
class carsome( Flask ):
	def __init__(self, import_name):
		super(carsome, self).__init__(import_name)
		self.config.from_pyfile('config/setting.py')
		db.init_app(self)



app = carsome(__name__)

manager = Manager(app)

login_manager = LoginManager()
# # login_manager.session_protection = 'strong'
# # login_manager.login_view = 'admin.login'
login_manager.init_app(app)
avatars = Avatars(app)

from common.libs.UrlManager import UrlManager
app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl, 'buildUrl')
app.add_template_global(UrlManager.buildImageUrl, 'buildImageUrl')



