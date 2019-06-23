# -*- coding: UTF-8 -*-
from flask import Blueprint, request, jsonify, redirect, url_for, redirect, render_template
from common.libs.Helper import getCurrentDate, ops_render, iPagination, getDictFilterField
from carsome import app, db
from common.models.vehicle.Vehicle import Vehicle
from common.models.vehicle.Vehiclecat import Vehiclecat
from common.models.vehicle.Car_change_log import StockChangeLog
from common.libs.UrlManager import UrlManager
from sqlalchemy import or_
from decimal import Decimal
from common.libs.FoodService import FoodService

route_admin_car = Blueprint('car', __name__)


@route_admin_car.route("/index")
def index ():
	resp_data = {}
	req = request.values
	query = Vehicle.query

	if 'status' in req and int(req['status']) > -1:
		query = query.filter(Vehicle.status == int(req['status']))

	list = query.order_by(Vehicle.id.desc()).all()
	resp_data['list'] = list

	return ops_render("admin/car/index.html", resp_data)


#
# @route_food.route( "/info" )
# def info():
#     resp_data = {}
#     req = request.args
#     id = int(req.get("id", 0))
#     reback_url = UrlManager.buildUrl("/food/index")
#
#     if id < 1:
#         return redirect( reback_url )
#
#     info = Food.query.filter_by( id =id ).first()
#     if not info:
#         return redirect( reback_url )
#
#     stock_change_list = FoodStockChangeLog.query.filter( FoodStockChangeLog.food_id == id )\
#         .order_by( FoodStockChangeLog.id.desc() ).all()
#
#     resp_data['info'] = info
#     resp_data['stock_change_list'] = stock_change_list
#     resp_data['current'] = 'index'
#     return ops_render( "food/info.html",resp_data )
#
#
@route_admin_car.route("/set", methods=['GET', 'POST'])
def set():
    if request.method == "GET":
        resp_data = {}
        req = request.args
        id = int( req.get('id',0) )
        info = Vehicle.query.filter_by( id = id ).first()
        if info and info.status != 1:
            return redirect( UrlManager.buildUrl("index") )

        cat_list = Vehiclecat.query.all()
        resp_data['info'] = info
        resp_data['cat_list'] = cat_list
        resp_data['current'] = 'index'
        return ops_render( "admin/car/caradd.html" ,resp_data)

    resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
    req = request.values
    id = int(req['id']) if 'id' in req and req['id'] else 0
    cat_id = int(req['cat_id']) if 'cat_id' in req else 0
    name = req['name'] if 'name' in req else ''
    price = req['price'] if 'price' in req else ''
    main_image = req['main_image'] if 'main_image' in req else ''
    summary = req['summary'] if 'summary' in req else ''
    stock = int(req['stock']) if 'stock' in req else ''
    tags = req['tags'] if 'tags' in req else ''

    if cat_id < 1:
        resp['code'] = -1
        resp['msg'] = "请选择分类~~"
        return jsonify(resp)

    if name is None or len(name) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的名称~~"
        return jsonify(resp)

    if not price or len( price ) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的售卖价格~~"
        return jsonify(resp)

    price = Decimal(price).quantize(Decimal('0.00'))
    if  price <= 0:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的售卖价格~~"
        return jsonify(resp)

    if main_image is None or len(main_image) < 3:
        resp['code'] = -1
        resp['msg'] = "请上传封面图~~"
        return jsonify(resp)

    if summary is None or len(summary) < 3:
        resp['code'] = -1
        resp['msg'] = "请输入图书描述，并不能少于10个字符~~"
        return jsonify(resp)

    if stock < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的库存量~~"
        return jsonify(resp)

    if tags is None or len(tags) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入标签，便于搜索~~"
        return jsonify(resp)


    model_food = Vehicle()
    model_food.status = 1
    model_food.created_time = getCurrentDate()

    model_food.cat_id = cat_id
    model_food.name = name
    # model_food.price = price
    # model_food.main_image = main_image
    model_food.summary = summary
    model_food.stock = stock
    model_food.tags = tags
    model_food.updated_time = getCurrentDate()

    db.session.add(model_food)
    db.session.commit()

    return jsonify(resp)


@route_admin_car.route("/cat")
def cat ():
	resp_data = {}
	req = request.values
	query = Vehiclecat.query

	if 'status' in req and int(req['status']) > -1:
		query = query.filter(Vehiclecat.status == int(req['status']))

	list = query.order_by(Vehiclecat.weight.desc(), Vehiclecat.id.desc()).all()
	resp_data['list'] = list
	resp_data['search_con'] = req
	resp_data['status_mapping'] = app.config['STATUS_MAPPING']
	resp_data['current'] = 'cat'
	return ops_render("food/cat.html", resp_data)


@route_admin_car.route("/cat-set", methods=["GET", "POST"])
def catSet ():
	if request.method == "GET":
		resp_data = {}
		req = request.args
		id = int(req.get("id", 0))
		info = None
		if id:
			info = Vehiclecat.query.filter_by(id=id).first()
		resp_data['info'] = info
		resp_data['current'] = 'cat'
		return ops_render("food/cat_set.html", resp_data)

	resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
	req = request.values

	id = req['id'] if 'id' in req else 0
	name = req['name'] if 'name' in req else ''
	weight = int(req['weight']) if ('weight' in req and int(req['weight']) > 0) else 1

	if name is None or len(name) < 1:
		resp['code'] = -1
		resp['msg'] = "请输入符合规范的分类名称~~"
		return jsonify(resp)

	food_cat_info = Vehiclecat.query.filter_by(id=id).first()
	if food_cat_info:
		model_food_cat = food_cat_info
	else:
		model_food_cat = Vehiclecat()
		model_food_cat.created_time = getCurrentDate()
	model_food_cat.name = name
	model_food_cat.weight = weight
	model_food_cat.updated_time = getCurrentDate()
	db.session.add(model_food_cat)
	db.session.commit()
	return jsonify(resp)
#
# @route_food.route("/cat-ops",methods = [ "POST" ])
# def catOps():
#     resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
#     req = request.values
#
#     id = req['id'] if 'id' in req else 0
#     act = req['act'] if 'act' in req else ''
#     if not id :
#         resp['code'] = -1
#         resp['msg'] = "请选择要操作的账号~~"
#         return jsonify(resp)
#
#     if  act not in [ 'remove','recover' ] :
#         resp['code'] = -1
#         resp['msg'] = "操作有误，请重试~~"
#         return jsonify(resp)
#
#     food_cat_info = FoodCat.query.filter_by( id= id ).first()
#     if not food_cat_info:
#         resp['code'] = -1
#         resp['msg'] = "指定分类不存在~~"
#         return jsonify(resp)
#
#     if act == "remove":
#         food_cat_info.status = 0
#     elif act == "recover":
#         food_cat_info.status = 1
#
#         food_cat_info.update_time = getCurrentDate()
#     db.session.add( food_cat_info )
#     db.session.commit()
#     return jsonify(resp)
#
# @route_food.route("/ops",methods=["POST"])
# def ops():
#     resp = { 'code':200,'msg':'操作成功~~','data':{} }
#     req = request.values
#
#     id = req['id'] if 'id' in req else 0
#     act = req['act'] if 'act' in req else ''
#
#     if not id :
#         resp['code'] = -1
#         resp['msg'] = "请选择要操作的账号~~"
#         return jsonify(resp)
#
#     if act not in [ 'remove','recover' ]:
#         resp['code'] = -1
#         resp['msg'] = "操作有误，请重试~~"
#         return jsonify(resp)
#
#     food_info = Food.query.filter_by( id = id ).first()
#     if not food_info:
#         resp['code'] = -1
#         resp['msg'] = "指定美食不存在~~"
#         return jsonify(resp)
#
#     if act == "remove":
#         food_info.status = 0
#     elif act == "recover":
#         food_info.status = 1
#
#     food_info.updated_time = getCurrentDate()
#     db.session.add(food_info)
#     db.session.commit()
#     return jsonify( resp )
#