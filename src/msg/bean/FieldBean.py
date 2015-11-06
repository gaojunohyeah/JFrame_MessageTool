#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = 'gaojun'

# 定义消息属性对象
# FieldBean
class FieldBean(object):
    def __init__(self, type, name, comment, fields, isList):
        self.type = type
        self.name = name
        self.comment = comment
        self.fields = fields
        self.isList = isList
