#!/usr/bin/env python
#! -*- coding: utf-8 -*-

from __future__ import absolute_import
import os
from flask import Flask
from flask_restful import Api
# from flask_jwt import JWT

from .handlers import ProductHandler
# from models import User

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'm9ruhppNu4OHQCtrsoez8woU')
# app.config['JWT_AUTH_URL_RULE'] = os.getenv('JWT_AUTH_URL_RULE', '/v1/auth')

api = Api(app, prefix="/v1")


# def verify(username, password):
#     if not (username and password):
#         return False
#     if USER_DATA.get(username) == password:
#         return User(name="Geraldo Andrade", email='geraldo@geraldoandrade.com')
#
#
# def identity(payload):
#     user_id = payload['identity']
#     return {"user_id": user_id}


# jwt = JWT(app, verify, identity)

api.add_resource(ProductHandler, '/products', '/products/<int:id>')
