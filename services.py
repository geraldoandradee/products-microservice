# -*- coding: utf-8 -*-
from .exceptions import PreconditionFailException, ProductAlreadyExistsException, ItemNotFoundException
from .models import Product
from .repository import db
from .validators import ProductValidator


class ProductService(object):

    def _validate(self, payload, is_a_patch=False):
        validator = ProductValidator(payload)
        validator.validate(is_a_patch)

    def create(self, payload):
        self._validate(payload)

        if 'id' in payload:
            item = self.read(payload['id'])
            if item:
                raise ProductAlreadyExistsException("Product already exists")
        else:
            raise PreconditionFailException("You must provide an ID")

        product = Product()
        product.__dict__.update(payload)
        db.save(payload)

        return self.read(payload['id'])

    def read(self, id, klass_reference=None):
        return db.get(id, klass_reference)

    def update(self, id, payload):
        self._save(id, payload)

        return self.read(id)

    def patch(self, id, payload):
        if not id:
            raise PreconditionFailException("Product id is required")

        product = self.read(id, Product)

        if not product:
            raise ItemNotFoundException("Product does not exists.")

        if 'id' in payload:
            del payload['id']

        product.__dict__.update(payload)
        self._validate(payload=payload, is_a_patch=True)
        db.save(product)

        return self.read(id)

    def list(self):
        return db.list()

    def delete(self, id):
        if id:
            return db.delete(id)
        raise PreconditionFailException("You must provide an id for deletion")

    def _save(self, id, payload):
        self._validate(payload)
        product = self.read(id, Product)
        del payload['id']

        product.__dict__.update(payload)

        return db.save(product)
