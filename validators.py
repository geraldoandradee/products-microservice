#! -*- coding: utf-8 -*-
import logging
from exceptions import InvalidFieldException


class ProductValidator(object):
    def __init__(self, data):
        self.data = data
        self.possible_fields = ['id', 'title', 'price']
        self.errors = []

    def is_valid_fields(self, field):
        if field not in self.possible_fields:
            raise InvalidFieldException("Product has not %s field" % field)
        return True

    def validate(self):
        for key, value in self.data.items():
            if self.is_valid_fields(key):
                getattr(self, ''.join(['_validate_', key]))(key, value)

    def _validate_id(self, key, value):
        try:
            int(value)
        except ValueError as e:
            logging.error("Invalid '%s' field: %s" % (key, e))
            raise InvalidFieldException("Invalid '%s' field")

    def _validate_title(self, key, value):
        if not value:
            raise InvalidFieldException("A Product must have a %s" % key)
        elif len(value) > 255:
            raise InvalidFieldException("A Product cannot have a '%s' greater than 255" % key)

    def _validate_price(self, key, value):
        if value <= 0.00:
            raise InvalidFieldException("A Product cannot have a '%s' lesser than 0.00" % key)
        try:
            float(value)
        except ValueError as e:
            logging.error("Invalid '%s' field: %s" % (key, e))
            raise InvalidFieldException("Product Price is not valid")
