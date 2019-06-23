# coding: utf-8
from flask import Flask
from sqlalchemy import Column, DateTime, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_manager, UserMixin, AnonymousUserMixin
from flask_login.login_manager import LoginManager
from sqlalchemy.schema import FetchedValue
from carsome import  app, db, login_manager
from flask_avatars import Identicon



class User(UserMixin,db.Model):
	__tablename__ = 'user'

	id = db.Column(db.Integer, primary_key=True, nullable=False)
	nickname = db.Column(db.String(32, 'utf8mb4_unicode_ci'))
	email = db.Column(db.String(64, 'utf8mb4_unicode_ci'), nullable=False)
	password = db.Column(db.String(255, 'utf8mb4_unicode_ci'), nullable=False)
	password_hash = db.Column(db.String(255))
	sign = db.Column(db.String(255, 'utf8mb4_unicode_ci'))
	status = db.Column(db.Integer)
	avatars = db.column(db.String(64))
	createtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
	updatetime = db.Column(db.DateTime)


	class Permission(db.Model):
		__tablename__ = 'permission'
		id = db.Column(db.Integer, primary_key=True, autoincrement=True)
		name = db.Column(db.String(32), unique=True, nullable=False)
		action= db.Column(db.String(128))

	class Menus(db.Model):
		__tablename__ = "menus"
		id = db.Column(db.Integer, primary_key=True, autoincrement=True)
		name = db.Column(db.String(32), unique=True)
		type = db.Column(db.String(64))
		order = db.Column(db.SmallInteger, default=0)



	def __init__ (self, **kwargs):
		super(User, self).__init__(**kwargs)
		self.generate_avatar()
		# self.follow(self)  # follow self
		self.set_role()

	def __repr__ (self):  # __repr__方法告诉Python如何打印class对象，方便我们调试使用。
		return '<User %r>' % (self.email)

	# @property                                       #映射用户uid为 flask-login  中get-id 找不到id的问题
	# def id (self):
	#     return self.uid

	@property
	def password (self):
		raise AttributeError('密码不是可读属性')

	@password.setter
	def password (self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password (self, password):
		return check_password_hash(self.password_hash, password)

	def is_authenticated (self):
		return True

	def is_active (self):
		return True

	def is_anonymous (self):
		return False

	# @property               # """必须返回用户的唯一表示符，使用 Unicode 编码字符串"""
	# def get_id (self):
	#     return self.id
	#
	# @login_manager.user_loader
	# def load_user (user_id):
	# 	return User.query.get(int(user_id))

	# 用户头像
	def generate_avater (self):
		avater = Identicon
		filenames = avater.generate(text=self.nickname)
		self.avatars = filenames[1]
		db.session.commit()

