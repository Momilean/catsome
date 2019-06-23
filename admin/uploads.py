# -*- coding: UTF-8 -*-
from flask import Blueprint,send_from_directory
from carsome import app
route_uploads = Blueprint('uploads', __name__)

@route_uploads.route("/<path:filename>")
def index( filename ):
    return send_from_directory(  app.root_path + "/uploads/" ,filename )