# -*- coding: UTF-8 -*-
from flask import Blueprint
route_api = Blueprint( 'api_page',__name__ )
from admin.api.Member import *
from admin.api.Vehicle import *
@route_api.route("/")
def index():
    return "Mina Api V1.0~~"