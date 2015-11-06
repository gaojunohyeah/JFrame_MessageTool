#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = 'gaojun'

import os


# 消息生成基类
# msgBean 消息结构数据对象
# templateFile 消息模板文件名称
# genPath 消息生成路径
# template 模板渲染对象
class BaseBuilder(object):
    def __init__(self, msgBean, temFile, genPath, fileName, env):
        self.msgBean = msgBean
        self.templateFile = temFile
        self.genPath = genPath
        self.fileName = fileName
        self.template = env.get_template(self.templateFile)

    # 生成消息文件基类方法
    def buildMsgFile(self):
        return True

    # 写入消息文件
    def genMsgFile(self, stream):
        # 路径不存在，则创建对应文件
        if not os.path.exists(self.genPath):
            os.makedirs(self.genPath)

        # 打开文件
        filePath = self.genPath + self.fileName
        print "write message file :", filePath
        file = open(filePath, "w")
        file.write(stream)
        file.close()

        return
