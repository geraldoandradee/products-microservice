#! -*- coding: utf-8 -*-
from flask import request
from flask_restful import Resource
import logging

# from flask_jwt import jwt_required
from exceptions import PreconditionFailException
from services import ProductService


class ProductHandler(Resource):

    def __init__(self):
        self.service = ProductService()
        super(ProductHandler, self).__init__()

    # @jwt_required()
    def get(self, id=None):
        if id is None:
            return self.service.list()
        else:
            item = self.service.read(id)
            if not item:
                return {}, 404
            return item

    def post(self):
        data = request.get_json()
        try:
            self.service.create(data)
            return {}, 201
        except Exception as e:
            logging.error("Cannot create a new Product %s" % e)
            return {"message": "Cannot create a new Product", "reason": "%s" % e}, 400

    def put(self, id):
        data = request.get_json()
        try:
            product = self.service.update(id, data)
            return product, 200
        except Exception as e:
            logging.error("Cannot create a new Product %s" % e)
            return {"message": "Cannot create a new Product"}, 400

    def patch(self, id):
        data = request.get_json()
        try:
            product = self.service.patch(id, data)
            return product, 200
        except Exception as e:
            logging.error("Cannot create a new Product %s" % e)
            return {"message": "Cannot patch a Product"}, 400

    def delete(self, id=None):
        try:
            self.service.delete(id)
        except PreconditionFailException as e:
            logging.error("Cannot delete data: %s" % e)
            return {"message": e}, 412
        except Exception as e:
            logging.error("Cannot delete data: %s" % e)

        return {}, 200
