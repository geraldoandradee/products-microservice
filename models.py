# -*- coding: utf-8 -*-


class Product(object):
    def __init__(self, id=None, title=None, price=None):
        self.id = id
        self.title = title
        self.price = price


class User(object):
    def __init__(self, name, email):
        self.id = email
        self.name = name
        self.email = email

    def __str__(self):
        return "User(id='%s')" % self.id
