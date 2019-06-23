# -*- coding: utf-8 -*-
import os
import sys
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))  #定义路径

DEBUG = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1/carsome'
# SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = "utf8mb4"

SECRET_KEY = '432432432432'

ALBUMY_UPLOAD_PATH = os.path.join(basedir, 'uploads')
AVATARS_SAVE_PATH = os.path.join(ALBUMY_UPLOAD_PATH, 'avatars')
AVATARS_SIZE_TUPLE = (30, 100, 200)

# #RbacMiddleware 过滤
URL_REGEX = '^{}$'
PASS_URL_LIST = [
    "^/login/",
    "^/static/",
    "^/api",
    "^/register/$",
]

#CAR APP配置文件
MINA_APP = {
    'appid':'wx2fb633a2451bca71',
    'appkey':'389b8059461e60f1b9905cbafdae1af2',
}

STATUS_MAPPING = {
    "1":"正常",
    "0":"已删除"
}

PAGE_SIZE = 50
PAGE_DISPLAY = 10


UPLOAD = {
    'ext':[ 'jpg','gif','bmp','jpeg','png' ],
    'prefix_path':'/uploads/',
    'prefix_url':'/uploads/'
}
APP = {
    'domain':'http://127.0.0.1:9080'
}
