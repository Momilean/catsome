# -*- coding: UTF-8 -*-
from admin.api import route_api
from flask import request, jsonify
from carsome import db
from common.models.vehicle.Vehicle import Vehicle
from common.models.vehicle.Vehiclecat import Vehiclecat
from common.libs.UrlManager import UrlManager


@route_api.route("/car/index")
def CarIndex ():
	resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
	cat_list = Vehiclecat.query.filter_by(status=1).order_by(Vehiclecat.weight.desc()).all()
	data_cat_list = []
	data_cat_list.append({
		'id': 0,
		'name': "全部"
	})
	if cat_list:
		for item in cat_list:
			tmp_data = {
				'id': item.id,
				'name': item.name
			}
			data_cat_list.append(tmp_data)
	resp['data']['cat_list'] = data_cat_list

	food_list = Vehicle.query.filter_by(status=1) \
		.order_by(Vehicle.id.desc()).limit(3).all()

	data_food_list = []
	if food_list:
		for item in food_list:
			tmp_data = {
				'id': item.id,
				'pic_url': UrlManager.buildImageUrl(item.main_image)
			}
			data_food_list.append(tmp_data)

	resp['data']['banner_list'] = data_food_list
	return jsonify(resp)
