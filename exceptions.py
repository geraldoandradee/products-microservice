#! -*- coding: utf-8 -*-


class InvalidFieldException(Exception):
    pass


class PreconditionFailException(Exception):
    pass


class ItemNotFoundException(Exception):
    pass


class ProductAlreadyExistsException(Exception):
    pass
