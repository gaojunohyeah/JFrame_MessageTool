#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = 'gaojun'

# 定义消息对象
# MessageBean
class MessageBean(object):
    def __init__(self, package):
        self.package = package

    def setType(self, type):
        self.type = type
        types = type.split("_")
        self.typeCS = types[0]
        self.typeName = types[1]

    def setName(self, name):
        self.name = name
        self.lowName = self.name[0].lower() + self.name[1:]
        self.cmd = self.package + "." + self.name

    def setId(self, id):
        self.id = id

    def setComment(self, comment):
        self.comment = comment

    def setFields(self, fields):
        self.fields = fields

    def setBase(self, base):
        if 'true' == base or True == base:
            self.base = True
        else:
            self.base = False

    def setAuth(self, auth):
        if 'true' == auth or True == auth:
            self.auth = True
        else:
            self.auth = False

    def setIsGm(self, isGm):
        if "1" == str(isGm):
            self.isGm = 1
        else:
            self.isGm = 0
