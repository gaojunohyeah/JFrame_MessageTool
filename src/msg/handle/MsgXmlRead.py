#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = 'gaojun'

import os
from xml.dom import minidom

from src.msg.bean import *


# 消息名称和ID字典，用于验证名称和ID的唯一性
MsgCmdDic = {}
MsgIdDic = {}


# 获取所有的消息配置路径
def getXmlFileList(xmlPath):
    # 列出所有文件
    files = os.listdir(xmlPath)
    xmlFiles = []
    # print files
    for file in files:
        truePath = xmlPath + "/" + file
        # 是文件且为xml文件
        if os.path.isfile(truePath) and truePath.endswith(".xml"):
            xmlFiles.append(truePath)

    return xmlFiles


# 加载所有的filed属性对象
def loadMsgFields(fieldNodes):
    fields = []

    # 循环所有 属性节点
    for fieldNode in fieldNodes:
        # 节点是field属性才行
        if "field" == fieldNode.nodeName:
            type = fieldNode.getAttribute('type')
            name = fieldNode.getAttribute('name')
            comment = fieldNode.getAttribute('comment')
            isList = False
            subfields = None

            # 该属性的类型是list
            if "list" == type:
                isList = True
                subfields = loadMsgFields(fieldNode.childNodes)  # .getElementsByTagName("field"))

            # 初始化属性对象
            fieldBean = FieldBean.FieldBean(type, name, comment, subfields, isList)
            fields.append(fieldBean)

    return fields


# 加载消息文件
def loadMsgFile(path):
    dom = minidom.parse(path)

    # 根节点
    root = dom.documentElement

    # 获取包名
    packageName = root.getAttribute('package')

    msgBeans = []

    # 获取消息体节点
    childs = root.getElementsByTagName("message")
    for child in childs:
        type = child.getAttribute('type')
        name = child.getAttribute('name')
        id = child.getAttribute('id')
        comment = child.getAttribute('comment')
        base = child.getAttribute('base')
        isGm = child.getAttribute('isGm')
        auth = child.getAttribute('auth')

        # 实例化 消息对象
        msgBean = MessageBean.MessageBean(packageName)
        msgBean.setType(type)
        msgBean.setName(name)
        msgBean.setId(id)
        msgBean.setComment(comment)
        msgBean.setBase(base)
        msgBean.setIsGm(isGm)
        msgBean.setAuth(auth)

        # 消息唯一性验证
        if MsgCmdDic.get(msgBean.cmd):
            raise Exception("message cmd repeat, the message cmd is", msgBean.cmd, " message id is", msgBean.id)
        else:
            MsgCmdDic[msgBean.cmd] = msgBean.id
        if MsgIdDic.get(msgBean.id):
            raise Exception("message id repeat, the message cmd is", msgBean.cmd, " message id is", msgBean.id)
        else:
            MsgIdDic[msgBean.id] = msgBean.cmd

        # 获取消息属性
        fields = loadMsgFields(child.childNodes)  # .getElementsByTagName("field"))
        # print fields
        msgBean.setFields(fields)

        msgBeans.append(msgBean)

    return msgBeans


# 加载所有消息配置
def loadMsgXML(msgPath):
    # 获取配置文件
    xmlFiles = getXmlFileList(msgPath)

    MsgCmdDic = {}
    MsgIdDic = {}

    # 消息文件加载
    msgBeans = []
    for path in xmlFiles:
        print "load message file :", path
        beans = loadMsgFile(path)
        for bean in beans:
            msgBeans.append(bean)
    return msgBeans
