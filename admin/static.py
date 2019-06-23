# -*- coding: UTF-8 -*-
from flask import Blueprint,send_from_directory
from carsome import app
route_static = Blueprint('static', __name__)

@route_static.route("/<path:filename>")
def index( filename ):
    return send_from_directory(  app.root_path + "/static/" ,filename )