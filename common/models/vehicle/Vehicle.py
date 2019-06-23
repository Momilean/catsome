# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, Numeric, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Vehicle(db.Model):
    __tablename__ = 'vehicle'

    id = db.Column(db.Integer, primary_key=True)
    cat_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    name = db.Column(db.String(100, 'utf8mb4_0900_ai_ci'), nullable=False, server_default=db.FetchedValue())
    car_models = db.Column(db.String(11, 'utf8mb4_0900_ai_ci'))
    price = db.Column(db.Numeric(10, 2), nullable=False, server_default=db.FetchedValue())
    mileage = db.Column(db.Integer, server_default=db.FetchedValue())
    license_plate = db.Column(db.String(30))
    license_time = db.Column(db.String(255, 'utf8mb4_0900_ai_ci'))
    transmission = db.Column(db.String(64))
    volume = db.Column(db.String(64, 'utf8mb4_0900_ai_ci'))
    summary = db.Column(db.String(10000), nullable=False, server_default=db.FetchedValue())
    main_image = db.Column(db.String(100, 'utf8mb4_0900_ai_ci'), nullable=False, server_default=db.FetchedValue())
    stock = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tags = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    comment_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
