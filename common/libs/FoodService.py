# -*- coding: utf-8 -*-
from carsome import app,db
from common.models.vehicle.Car_change_log import StockChangeLog
from common.models.vehicle.Vehicle import Vehicle
from common.libs.Helper import getCurrentDate
class FoodService():

    @staticmethod
    def setStockChangeLog( food_id = 0,quantity = 0,note = '' ):

        if food_id < 1:
            return False

        food_info = Vehicle.query.filter_by( id = food_id ).first()
        if not food_info:
            return False

        model_stock_change = StockChangeLog()
        model_stock_change.food_id = food_id
        model_stock_change.unit = quantity
        model_stock_change.total_stock = food_info.stock
        model_stock_change.note = note
        model_stock_change.created_time = getCurrentDate()
        db.session.add(model_stock_change)
        db.session.commit()
        return True


