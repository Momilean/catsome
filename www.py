from flask import Flask
from carsome import app


from admin.auth.user import route_admin
from admin.main.Index import route_admin_main
from admin.car.index import route_admin_car
from admin.api.Member import route_api
from admin.static import route_static
from admin.upload.Upload import route_admin_upload
from admin.uploads import route_uploads

app.register_blueprint(route_api, url_prefix="/api")
app.register_blueprint(route_admin_upload, url_prefix="/upload")
app.register_blueprint(route_static, url_prefix="/static")
app.register_blueprint(route_uploads,url_prefix="/uploads")
app.register_blueprint(route_admin, url_prefix="/admin")
app.register_blueprint(route_admin_main, url_prefix="/admin/main")
app.register_blueprint(route_admin_car, url_prefix="/admin/car")